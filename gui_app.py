import app_status
import os
import time
import manage_log as log
import flet as ft
import connect_chatgpt as gpt

global character
global display_name
global my_status
global service_stop_flag
global audio_input_flag

# main.pyでchatgptを呼び出すための設定
global chatgpt_status
# chatgptからのレスポンスを表示する
global chatgpt_response

max_image_num = {}
now_image_num = 0

async def main(page: ft.Page):
    global audio_input_flag

    # 0.6秒おきに行われる定期実行
    async def regular_exection():
        global now_image_num
        global chatgpt_response

        while not service_stop_flag:
            # 表情がコマ送りで変化する
            img_path, now_image_num = get_image(now_image_num)
            img.src = img_path

            # チャットの返信を表示する
            response_field.value = chatgpt_response

            # 送信ボタンを押せるかどうかのチェック
            send_talk_button.disabled = is_state_normal()
            send_objection_button.disabled = is_state_normal()

            await page.update_async()
            time.sleep(0.6)

    # 会話内容をログに追加する
    async def add_message(e):
        message = question_field.value
        question_field.value = ''
        log.write_message_log(message)
    
    # 会話内容をログに追加してchatgptにメッセージを送信する
    def call_talk_chatgpt(e):
        global chatgpt_status
        message = question_field.value
        question_field.value = ''
        log.write_message_log(message)
        chatgpt_status = app_status.ChatGPTStatus.TALK
    
    def call_objection_chatgpt(e):
        global chatgpt_status
        message = question_field.value
        question_field.value = ''
        log.write_message_log(message)
        chatgpt_status = app_status.ChatGPTStatus.OBJECTION
    
    # 終了確認のダイアログが開く
    async def open_finish_dialog(e):
        page.dialog = finish_confilm_dialog
        finish_confilm_dialog.open = True
        await page.update_async()

    async def finish_service(e):
        global service_stop_flag
        service_stop_flag = True
        
        finish_confilm_dialog.open = False
        page.dialog = finish_dialog
        finish_dialog.open = True
        await page.update_async()

        # TODO: destroy()メソッドが動作しない
        # await page.window_destroy()

    def cancel_finish(e):
        finish_confilm_dialog.open = False
        page.update_async()

    # 表情画像の基本設定
    global now_image_num
    img_path, now_image_num = get_image(now_image_num)
    img = ft.Image(
        src = img_path,
        height=400,
        fit=ft.ImageFit.CONTAIN,
    )

    # 音声入力を受け入れるフラグを切り替える
    def change_audio_input_flag(e):
        global audio_input_flag
        audio_input_flag = not audio_input_flag

    # normal状態の時以外は送信ボタンを押せないようにしている
    def is_state_normal():
        global my_status
        return my_status != app_status.Status.NORMAL

    # ページの基本構成の設定
    page.title = "金沢キューピッド"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.window_width = 600
    page.window_height = 600
    await page.update_async()
    display_name_text = ft.Text(display_name, size=30, color=ft.colors.BLUE_400)
    question_field = ft.TextField(label="会話内容", width=250, border_color=ft.colors.BLUE_100)
    add_button = ft.ElevatedButton("会話を追加する", on_click=add_message, width=170)
    send_talk_button = ft.ElevatedButton("君はどう思う？", on_click=call_talk_chatgpt, width=170)
    # send_objection_button = ft.ElevatedButton("反論して！", on_click=call_objection_chatgpt, width=170)
    send_objection_button = ft.ElevatedButton("君はどう思う？", on_click=call_objection_chatgpt, width=170)
    audio_input_switch = ft.Switch(label="音声入力", value=audio_input_flag, on_change=change_audio_input_flag)
    
    # chatgpt返信用の画面
    response_field = ft.TextField(label="ここに返信が届くよ！", border=ft.InputBorder.NONE)
    response_area = ft.Column([response_field], auto_scroll=True, height=50)

    # サービスを終了するためのコンポーネント
    finish_button = ft.ElevatedButton("会話を終了する", on_click=open_finish_dialog, width=170)
    finish_confilm_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("金沢キューピッド"),
        content=ft.Text("サービスを終了してもよいですか？"),
        actions=[
            ft.TextButton("はい", on_click=finish_service),
            ft.TextButton("いいえ", on_click=cancel_finish),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    finish_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("金沢キューピッド"),
        content=ft.Text("サービスを終了しました。×を押してアプリを終了してください。"),
    )

    # 画面構成
    # button_area = ft.Column([display_name_text, question_field, audio_input_switch, add_button, send_talk_button,send_objection_button, finish_button])
    button_area = ft.Column([display_name_text, question_field, audio_input_switch, add_button, send_objection_button, finish_button])
    under_area  = ft.Row([img, button_area])
    main_area = ft.Column([response_area, under_area])
    await page.add_async(main_area)

    # ステータスに応じた標準差分を設定する
    await regular_exection()
    
def get_image(now_image_num):
    now_image_num += 1
    if now_image_num >= max_image_num[my_status.value]:
        now_image_num = 0
    
    img_path = f'img/{character}/{my_status.value}/{character}_{my_status.value}_{now_image_num}.png'
    return img_path, now_image_num

def init(character_tmp):
    # アプリのキャラクターを設定する
    global character
    character = app_status.Character[character_tmp].value

    # アプリのディスプレイ名を設定する
    global display_name
    display_name = app_status.DisplayName[character_tmp].value

    # 各statusのフォルダの中にあるimageの数を取得してmax_image_numに格納する
    # 例: max_image_num = {'normal':2, 'speak':3, 'think':2}
    for status in app_status.Status:
        path = f'img/{character}/{status.value}'
        image_num =  sum(os.path.isfile(os.path.join(path,name)) for name in os.listdir(path))
        max_image_num[status.value] = image_num

    # chatgptを呼び出すための設定を初期化する
    global chatgpt_status
    chatgpt_status = app_status.ChatGPTStatus.NONE

    # サービスを終了させるためのフラグをセットする
    # 初期値はFalse
    global service_stop_flag
    service_stop_flag = False

    # 音声入力を受け付けるためのフラグ
    # 初期値はFalse
    global audio_input_flag
    audio_input_flag = True

    # chatgpt空の返信文をセットする
    # 初期値は空文字
    global chatgpt_response
    chatgpt_response = ""

def start():
    ft.app(target=main)