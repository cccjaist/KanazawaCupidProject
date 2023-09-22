import app_status
import os
import time
import flet as ft

global character
global my_status
global service_stop_flag
global service_progress

# main.pyでchatgptを呼び出すための設定
global chatgpt_flag
global chatgpt_text

max_image_num = {}
now_image_num = 0

async def main(page: ft.Page):

    # 表情が0.6秒ごとにコマ送りで変化する
    async def change_image():
        global now_image_num
        while not service_stop_flag:
            img_path, now_image_num = get_image(now_image_num)
            img.src = img_path
            await page.update_async()
            time.sleep(0.6)
    
    # ボタンがクリックされたらchatgptにメッセージを送信する
    async def call_chatgpt(e):
        global my_status
        global chatgpt_flag
        global chatgpt_text

        chatgpt_text = question.value
        chatgpt_flag = True
    
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
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )

    # ページの基本構成の設定
    page.title = "金沢キューピッド"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50
    await page.update_async()
    question = ft.TextField(label="会話内容")
    send_button = ft.ElevatedButton("君はどう思う？", on_click=call_chatgpt)
    
    # サービスを終了するためのコンポーネント
    finish_button = ft.ElevatedButton("会話を終了する", on_click=open_finish_dialog)
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

    await page.add_async(img, question, send_button, finish_button)

    # ステータスに応じた標準差分を設定する
    await change_image()
    
def get_image(now_image_num):
    now_image_num += 1
    if now_image_num >= max_image_num[my_status.value]:
        now_image_num = 0
    
    img_path = f'img/{character.value}/{my_status.value}/{character.value}_{my_status.value}_{now_image_num}.png'
    return img_path, now_image_num

def init():
    # 各statusのフォルダの中にあるimageの数を取得してmax_image_numに格納する
    # 例: max_image_num = {'normal':2, 'speak':3, 'think':2}
    for status in app_status.Status:
        path = f'img/{character.value}/{status.value}'
        image_num =  sum(os.path.isfile(os.path.join(path,name)) for name in os.listdir(path))
        max_image_num[status.value] = image_num

    # chatgptを呼び出すための設定を初期化する
    global chatgpt_flag
    global chatgpt_text
    chatgpt_flag = False
    chatgpt_text = ""

    # サービスを終了させるためのフラグをセットする
    # 初期値はFalse
    global service_stop_flag
    service_stop_flag = False

def start():
    ft.app(target=main)