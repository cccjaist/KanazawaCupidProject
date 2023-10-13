import json
import requests
import simpleaudio
import speech_recognition as sr
import app_status

VOICEVOX_ADDRESS = 'http://127.0.0.1:50021/'

global recognizer
# main.pyでchatgptを呼び出すための処理
global chatgpt_flag
# 話者の声を設定する変数
global speaker

# 会話の音声を聞いて変換処理に受け渡す処理
def speech_recognize(executor, log):
    global recognizer
    with sr.Microphone() as source:
        print('listen…')
        audio = recognizer.listen(source, phrase_time_limit=6)

        # 音声認識処理をスレッドに追加する
        executor.submit(recognize, audio, log)

# Google Web Speech APIで音声認識し、それをログに追加する処理
def recognize(audio, log):
    text = ''
    try:
        # Google Web Speech APIで音声認識を行い、その結果をログに書く
        text = recognizer.recognize_google(audio, language='ja-JP')
        log.write_message_log(text)
    except sr.UnknownValueError:
        pass
        # log.write_error_log('Google Web Speech APIは音声を認識できませんでした。')
    except sr.RequestError as e:
        log.write_error_log('GoogleWeb Speech APIに音声認識を要求できませんでした。')

def text_2_wav(text, log, max_retry=20, filename='audio.wav'):
    global speaker

    # 音声合成のための、クエリを作成
    query_payload = {'text': text, 'speaker': speaker}
    for _ in range(max_retry):
        response = requests.post(VOICEVOX_ADDRESS + 'audio_query', params=query_payload, timeout=30)
        if response.status_code == 200:
            query_data = response.json()
            break
    else:
        log.write_error_log('リトライ回数が上限に到達しました。')

    # 音声合成データの作成して、wavファイルに保存
    synth_payload = {'speaker': speaker}
    for _ in range(max_retry):
        response = requests.post(VOICEVOX_ADDRESS + 'synthesis', params=synth_payload, data=json.dumps(query_data), timeout=60)
        if response.status_code == 200:
            with open(filename, 'wb') as fp:
                fp.write(response.content)
            break
    else:
        log.write_error_log('リトライ回数が上限に到達しました。')

def play_auido_by_filename(filename: str):
    # 保存したwavファイルを再生する
    print('playing…')
    wav_obj = simpleaudio.WaveObject.from_wave_file(filename)
    play_obj = wav_obj.play()
    play_obj.wait_done()

def init(speaker_id):
    global recognizer
    global chatgpt_flag
    global speaker
    recognizer = sr.Recognizer()
    chatgpt_flag = False
    speaker = speaker_id
