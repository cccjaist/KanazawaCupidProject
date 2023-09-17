import my_speech_recognition as my_sr

def main():
    while True:
        # 音声をテキスト情報に変換
        text = my_sr.get_speech_recognize()
        print(text)

        filename = 'audio.wav'  # 音声データのファイル名
        my_sr.text_2_wav(text, filename=filename)
        my_sr.play_auido_by_filename(filename)

if __name__ == '__main__':
    main()