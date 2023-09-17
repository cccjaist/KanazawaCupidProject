import my_speech_recognition as my_sr

def main():
    while True:
        # 音声をテキスト情報に出力
        text = my_sr.get_speech_recognize()
        print(text)

if __name__ == '__main__':
    main()