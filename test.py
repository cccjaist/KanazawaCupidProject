import json
import requests
import simpleaudio
import speech_recognition as sr

while True:
    # 音声入力
    recognizer = sr.Recognizer()

    text = ''
    print('何か話してください…')
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        # Google Web Speech APIで音声認識
        text = recognizer.recognize_google(audio, language='ja-JP')
    except sr.UnknownValueError:
        print("Google Web Speech APIは音声を認識できませんでした。")
    except sr.RequestError as e:
        print("GoogleWeb Speech APIに音声認識を要求できませんでした;"
            " {0}".format(e))