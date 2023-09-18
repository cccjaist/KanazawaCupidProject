# 参考にしたサイト
# https://miyukimedaka.com/2020/06/14/0144-speech-recognition-synthesis/
# https://zero-cheese.com/11452/

import json
import requests
import simpleaudio
import speech_recognition as sr

def get_speech_recognize():
    # 音声入力
    recognizer = sr.Recognizer()
    
    text = ""
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        # Google Web Speech APIで音声認識
        text = recognizer.recognize_google(audio, language="ja-JP")
    except sr.UnknownValueError:
        print("Google Web Speech APIは音声を認識できませんでした。")
    except sr.RequestError as e:
        print("GoogleWeb Speech APIに音声認識を要求できませんでした;"
            " {0}".format(e))
    
    return text

# TODO: spkaker_id用の設定ファイル作る
def text_2_wav(text, speaker_id=8, max_retry=20, filename='audio.wav'):
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
        raise ConnectionError('リトライ回数が上限に到達しました。')

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
        raise ConnectionError('リトライ回数が上限に到達しました。')


def play_auido_by_filename(filename: str):
    # 保存したwavファイルを、再生
    wav_obj = simpleaudio.WaveObject.from_wave_file(filename)
    play_obj = wav_obj.play()
    play_obj.wait_done()
