from concurrent.futures import ThreadPoolExecutor
import my_speech_recognition as my_sr
import connect_chatgpt as chatgpt
import app_status
import gui_app as app
import manage_log as log
import time

def main():
    # サービスに必要な情報を初期化
    init()

    # 音声入力を監視する処理とアプリからの入力を監視する処理
    # マルチスレッドで呼び出す
    executor = ThreadPoolExecutor(max_workers=100)
    executor.submit(check_send_message)
    executor.submit(monitor_voice, executor)

    # サービスの開始
    start()

# 各ライブラリ・変数の初期化
def init():
    app.my_status = app_status.Status.NORMAL
    app.character = app_status.Character.ZUNDAMON
    log.init()
    my_sr.init()
    chatgpt.init()
    app.init()

# サービスの開始
def start():
    app.start()

# 音声入力を監視する
# 音声入力によるchatGPTの呼び出しが行われた場合
def monitor_voice(executor):
    while True:
        # アプリでservice_stop_flagが動作したらサービスが終了する
        if (app.service_stop_flag):
            break
        # 音声をテキスト情報に変換する処理を呼び出す
        my_sr.speech_recognize(executor, log)

def get_message():
    message_log = ''
    with open(log.get_file_name(), encoding='shift_jis') as f:
        message_log = f.read()
    return message_log

# chatGPTの呼び出しを監視する
def check_send_message():
    while True:
        send_message = ''

        # アプリでservice_stop_flagが動作したらサービスが終了する
        if (app.service_stop_flag):
            break
        
        # chatGPTを呼び出すフラグが立ったら呼び出しを行う
        if (app.chatgpt_flag):
            app.chatgpt_flag = False
            send_message = get_message()
        elif (my_sr.chatgpt_flag):
            my_sr.chatgpt_flag = False
            send_message = get_message()

        # chatGPTの返答待ちの場合は送信処理を行わない
        if send_message != '' and app.my_status != app_status.Status.THINK:
            app.my_status = app_status.Status.THINK

            # chatGPTからの返答を取得し、それを音声出力する  
            response = chatgpt.get_response(send_message)
            speak_message(response)

# chatGPTからの返答を音声出力する
def speak_message(message):
    # アプリのステータスをSPEAKにする
    app.my_status = app_status.Status.SPEAK

    # 音声データのファイル名
    filename = 'audio.wav'
    my_sr.text_2_wav(message, filename=filename)
    my_sr.play_auido_by_filename(filename)

if __name__ == '__main__':
    main()