from concurrent.futures import ThreadPoolExecutor
import my_speech_recognition as my_sr
import connect_chatgpt as chatgpt
import app_status
import gui_app as app
import manage_log as log

def main():
    try: 
        # サービスに必要な情報を初期化
        init()

        # 音声入力を監視する処理とアプリからの入力を監視する処理
        # マルチスレッドで呼び出す
        executor = ThreadPoolExecutor(max_workers=100)
        executor.submit(check_send_message, executor)
        executor.submit(monitor_voice, executor)

        # サービスの開始
        start()
    except Exception as e:
        log.write_error_log(e)

# 各ライブラリ・変数の初期化
def init():
    app.my_status = app_status.Status.NORMAL
    app.character = app_status.Character.ZUNDAMON
    log.init()
    my_sr.init()
    chatgpt.init(app_status.Prompt.NORMAL)
    app.init()

# サービスの開始
def start():
    app.start()

# 音声入力を継続的に監視する処理を呼び出す
def monitor_voice(executor):
    while True:
        # アプリでservice_stop_flagが動作したらサービスが終了する
        if (app.service_stop_flag):
            break
        # 音声をテキスト情報に変換する処理を呼び出す
        my_sr.speech_recognize(executor, log)

# chatgptに送信するメッセージ内容を取得する
def get_message():
    message_log = ''
    with open(log.get_tmp_file_name(), encoding='utf-8') as f:
        message_log = f.read()
    return message_log

# chatGPTの呼び出しを監視する
def check_send_message(executor):
    while True:
        send_message = ''

        # アプリでservice_stop_flagが動作したらサービスが終了する
        if (app.service_stop_flag):
            log.delete_tmp_file()
            break

        # chatGPTを呼び出すフラグが立ったら呼び出しを行う
        if (app.chatgpt_flag):
            app.chatgpt_flag = False
            send_message = get_message()
            print(send_message)
        if (my_sr.chatgpt_flag):
            my_sr.chatgpt_flag = False
            send_message = get_message()

        # chatGPTの返答待ちの場合は送信処理を行わない
        if send_message != '' and app.my_status != app_status.Status.THINK:
            print('送信処理開始')

            app.start_disp_progress_flag = True
            app.my_status = app_status.Status.THINK

            # chatGPTからの返答を取得し、それを音声出力する
            response = chatgpt.get_response(send_message, log)
            # タイムアウトなどでエラーが発生した際は、エラーメッセージを送信する
            if (response == ''):
                executor.submit(speak_error_message)
            else:
                executor.submit(speak_message, response)
            
            # tmpファイルの会話内容をlogに統合する
            log.attach_message_log()

# chatGPTからの返答を音声出力する
def speak_message(message):

    # 音声データのファイル名
    filename = 'audio.wav'
    try:
        my_sr.text_2_wav(message, log, filename=filename)
        # アプリのステータスをSPEAKにする
        app.my_status = app_status.Status.SPEAK
        my_sr.play_auido_by_filename(filename)
        app.my_status = app_status.Status.NORMAL
        app.finish_disp_progress_flag = False
    except Exception as e:
        log.write_error_log(e)
        speak_error_message()

# エラーメッセージを音声出力する
def speak_error_message():
    filename = 'error_message.wav'

    # アプリのステータスをSPEAKにする
    app.my_status = app_status.Status.SPEAK
    my_sr.play_auido_by_filename(filename)
    app.my_status = app_status.Status.NORMAL

if __name__ == '__main__':
    main()