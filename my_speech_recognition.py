# 参考にしたURL
# https://miyukimedaka.com/2020/06/14/0144-speech-recognition-synthesis/
import speech_recognition as sr

def get_speech_recognize():
    # 音声入力
    recognizer = sr.Recognizer()
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