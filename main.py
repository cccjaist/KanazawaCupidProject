from concurrent.futures import ThreadPoolExecutor
import my_speech_recognition as my_sr
import connect_chatgpt as chatgpt
import app_status
import gui_app as app
import time

def main():
    init()

    executor = ThreadPoolExecutor(max_workers=2)
    executor.submit(test)

    start()

def init():
    app.my_status = app_status.Status.NORMAL
    app.character = app_status.Character.ZUNDAMON
    chatgpt.init()
    app.init()

def start():
    app.start()

def monitor_voice():
    while True:
        # アプリでseevice_stop_flagが動作したらサービスが終了する
        if (app.service_stop_flag):
            print("finish")
            break
        
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

def test():
    while True:
        if (app.service_stop_flag):
            print("finish")
            break
        print("aaaaaaaaa")
        time.sleep(3)

if __name__ == '__main__':
    main()