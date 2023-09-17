import my_speech_recognition as my_sr
import connect_chatgpt as chatgpt

def main():
    init()

    while True:
        # 音声をテキスト情報に変換
        text = my_sr.get_speech_recognize()
        print(text)

        # 音声情報をchatGPTに送信
        ans = chatgpt.get_response(text)
        print("ans:")
        print(ans)

        filename = 'audio.wav'  # 音声データのファイル名
        my_sr.text_2_wav(ans, filename=filename)
        my_sr.play_auido_by_filename(filename)

def init():
    chatgpt.init()

if __name__ == '__main__':
    main()