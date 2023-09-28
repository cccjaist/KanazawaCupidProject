# 参考にしたサイト
# https://miyukimedaka.com/2020/06/14/0144-speech-recognition-synthesis/
# https://zero-cheese.com/11452/

import json
import requests
import simpleaudio
import speech_recognition as sr

CALLING_CHATGPT_MESSAGE = ['君はどう思う', '君はどうおもう', 'きみはどう思う', 'きみはどうおもう']

global recognizer
# main.pyでchatgptを呼び出すための処理
global chatgpt_flag

# 会話の音声を聞いて変換処理に受け渡す処理
def speech_recognize(executor, log):
    global recognizer
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

        # 音声認識処理をスレッドに追加する
        executor.submit(recognize, audio, log)

# Google Web Speech APIで音声認識し、それをログに追加する処理
def recognize(audio, log):
    text = ''
    try:
        # Google Web Speech APIで音声認識を行い、その結果をログに書く
        text = recognizer.recognize_google(audio, language='ja-JP')
        log.write_message_log(text)
        # もし会話内容に呼び出しコマンドが含まれていた場合は、chatGPTの呼び出しフラグをONにする
        for calling_catgpt_message in CALLING_CHATGPT_MESSAGE:
            if calling_catgpt_message in text:
                global chatgpt_flag
                chatgpt_flag = True
                break
    except sr.UnknownValueError:
        log.write_error_log('Google Web Speech APIは音声を認識できませんでした。')
    except sr.RequestError as e:
        log.write_error_log('GoogleWeb Speech APIに音声認識を要求できませんでした。')

# TODO: spkaker_id用の設定ファイル作る
def text_2_wav(text, log, speaker_id=8, max_retry=20, filename='audio.wav'):
    # 音声合成のための、クエリを作成
    query_payload = {"text": text, "speaker": speaker_id}
    for query_i in range(max_retry):
        response = requests.post("http://localhost:50021/audio_query",
                                 params=query_payload,
                                 timeout=10)
        if response.status_code == 200:
            query_data = response.json()
            break
    else:
        log.write_error_log('リトライ回数が上限に到達しました。')

    # 音声合成データの作成して、wavファイルに保存
    synth_payload = {"speaker": speaker_id}
    for synth_i in range(max_retry):
        response = requests.post("http://localhost:50021/synthesis",
                                 params=synth_payload,
                                 data=json.dumps(query_data),
                                 timeout=10)
        if response.status_code == 200:
            with open(filename, "wb") as fp:
                fp.write(response.content)
            break
    else:
        log.write_error_log('リトライ回数が上限に到達しました。')

def play_auido_by_filename(filename: str):
    # 保存したwavファイルを、再生
    wav_obj = simpleaudio.WaveObject.from_wave_file(filename)
    play_obj = wav_obj.play()
    play_obj.wait_done()

def init():
    global recognizer
    global chatgpt_flag
    recognizer = sr.Recognizer()
    chatgpt_flag = False
