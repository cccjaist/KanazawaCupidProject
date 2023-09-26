from concurrent.futures import ThreadPoolExecutor
import my_speech_recognition as my_sr
import connect_chatgpt as chatgpt
import app_status
import gui_app as app
import manage_log as log
import time

global executor

def main():
    # サービスに必要な情報を初期化
    init()

    # 音声入力を監視する処理とアプリからの入力を監視する処理
    # マルチスレッドで呼び出す
    global executor
    executor = ThreadPoolExecutor()
    executor.submit(monitor_voice)
    # executor.submit(send_message_from_app)

    # サービスの開始
    start()

# 各ライブラリ・変数の初期化
def init():
    app.my_status = app_status.Status.NORMAL
    app.character = app_status.Character.ZUNDAMON
    log.init()
    chatgpt.init()
    my_sr.init()
    app.init()

# サービスの開始
def start():
    app.start()

# 音声入力を監視する
# 音声入力によるchatGPTの呼び出しが行われた場合
def monitor_voice():
    while True:
        # アプリでservice_stop_flagが動作したらサービスが終了する
        if (app.service_stop_flag):
            break
        
        # 音声をテキスト情報に変換しログに残す
        my_sr.speech_recognize(executor, log)

        # send_message_to_chatgpt()

# アプリケーションのボタンによるchatGPTの呼び出しを監視する
def send_message_from_app():
    while True:
        # アプリでservice_stop_flagが動作したらサービスが終了する
        if (app.service_stop_flag):
            return
        
        # chatGPTを呼び出すフラグが立ったら呼び出しを行う
        if (app.chatgpt_flag):
            app.chatgpt_flag = False
            send_message = app.chatgpt_text

            # chatGPTからの返答を取得し、それを音声出力する
            speak_message(send_message_to_chatgpt(send_message))

# chatGPTへメッセージを送信して受け取る
def send_message_to_chatgpt(message):
    # chatGPTの返答待ちまたは空文字を送信する場合は送信処理を行わない
    if app.my_status == app_status.Status.THINK or message == '':
        return
    
    app.my_status = app_status.Status.THINK

    # 会話の内容をログに残す
    log.write_message_log(message)

    # 通信処理
    time.sleep(10)

    # TODO: chatgptに流す際はこのreturnを外す
    return "hogehoge"
    res = chatgpt.get_response(message)
    return res

# chatGPTからの返答を音声出力する
def speak_message(message):
    # アプリのステータスをSPEAKにする
    app.my_status = app_status.Status.SPEAK

    # 音声データのファイル名
    filename = 'audio.wav'
    my_sr.text_2_wav(message, log, filename=filename)
    my_sr.play_auido_by_filename(filename)

if __name__ == '__main__':
    main()