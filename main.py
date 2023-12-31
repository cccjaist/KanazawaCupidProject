from concurrent.futures import ThreadPoolExecutor
import my_speech_recognition as my_sr
import connect_chatgpt as chatgpt
import app_status
import gui_app as app
import manage_log as log
import time
import random

def main():
    try:
        # 利用したいキャラクターを選択する
        my_character = choose_character()

        # サービスに必要な情報を初期化
        init(app_status.Character[my_character].name)

        # 音声入力を監視する処理とアプリからの入力を監視する処理
        # マルチスレッドで呼び出す
        executor = ThreadPoolExecutor(max_workers=100)
        # これを入れると他の動作が重くなるのでコメントアウト
        # TODO: 後で直す
        # executor.submit(output_facilitation_message)
        executor.submit(check_send_message, executor)
        executor.submit(monitor_voice, executor)

        # サービスの開始
        start()
    except Exception as e:
        log.write_error_log(e, 1)

# 使用するキャラクターを選択する
def choose_character():
    print('----------------------------')
    print('You can use these characters.')
    character_list = list(app_status.DisplayName)
    while True:
        for i in range(len(character_list)):
            print(i, ':', character_list[i].value)
        character_num = input('Input the character number>>')

        try:
            my_character = character_list[int(character_num)].name
            return my_character
        except Exception as e:
            print('your input is invalid. Try again.')

# 各ライブラリ・変数の初期化
def init(character):
    app.my_status = app_status.Status.NORMAL
    log.init()
    my_sr.init(app_status.Speaker[character].value)
    chatgpt.init(character)
    app.init(character)

# サービスの開始
def start():
    app.start()

# 定期時間ごとにメッセージを出力する
def output_facilitation_message():
    while True:
        # アプリでservice_stop_flagが動作したらサービスが終了する
        # 420秒間は待機
        for i in range(420):
            if (app.service_stop_flag):
                return
            time.sleep(1)
        # 420秒経過したら通知音を鳴らし、メッセージ一覧の中からランダムでメッセージを出す
        message = app_status.facilitation_message
        app.chatgpt_response = message[random.randint(0, len(message) - 1)]
        print(app.chatgpt_response)
        my_sr.play_auido_by_filename('sound/notification.wav')

# 音声入力を継続的に監視する処理を呼び出す
def monitor_voice(executor):
    while True:
        # アプリでservice_stop_flagが動作したらサービスが終了する
        if (app.service_stop_flag):
            break
        # 音声をテキスト情報に変換する処理を呼び出す
        if (app.audio_input_flag):
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
        if app.chatgpt_status != app_status.ChatGPTStatus.NONE and app.my_status == app_status.Status.NORMAL:
            send_message = get_message()

        # chatGPTの返答待ちの場合は送信処理を行わない
        if send_message != '':
            print('送信処理開始')

            app.my_status = app_status.Status.THINK

            # chatGPTからの返答を取得し、それを音声出力する
            response = chatgpt.get_response(send_message, app.chatgpt_status, log)
            # タイムアウトなどでエラーが発生した際は、エラーメッセージを送信する
            if (response == ''):
                executor.submit(speak_error_message)
            else:
                app.chatgpt_response = response
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
        app.chatgpt_status = app_status.ChatGPTStatus.NONE
    except Exception as e:
        log.write_error_log(e,2)
        speak_error_message()
    
        app.chatgpt_status = app_status.ChatGPTStatus.NONE
        app.my_status = app_status.Status.NORMAL

# エラーメッセージを音声出力する
def speak_error_message():
    filename = 'sound/error_message.wav'

    # アプリのステータスをSPEAKにする
    app.my_status = app_status.Status.SPEAK
    my_sr.play_auido_by_filename(filename)
    app.my_status = app_status.Status.NORMAL

if __name__ == '__main__':
    main()