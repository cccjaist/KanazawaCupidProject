import app_status
import os
import time
from concurrent.futures import ThreadPoolExecutor
import flet as ft

global character
global my_status

max_image_num = {}
now_image_num = 0

async def main(page: ft.Page):

    # 表情画像の基本設定
    global now_image_num
    img_path, now_image_num = get_image(now_image_num)
    img = ft.Image(
        src = img_path,
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )
    
    async def change_image():
        global now_image_num
        while True:
            img_path, now_image_num = get_image(now_image_num)
            img.src = img_path
            await page.update_async()
            time.sleep(0.6)
    
    async def send_message(e):
        global my_status
        my_status = app_status.Status.THINK

    # ページの基本構成の設定
    page.title = "金沢キューピッド"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50
    await page.update_async()
    question = ft.TextField(label="会話内容")
    send_button = ft.ElevatedButton("君はどう思う？", on_click=send_message)
    await page.add_async(img, question, send_button)

    # ステータスに応じた標準差分を設定する
    await change_image()
    
def get_image(now_image_num):
    now_image_num += 1
    if now_image_num >= max_image_num[my_status.value]:
        now_image_num = 0
    
    img_path = f'img/{character.value}/{my_status.value}/{character.value}_{my_status.value}_{now_image_num}.png'
    print(img_path)
    return img_path, now_image_num

def init():
    # 各statusのフォルダの中にあるimageの数を取得してmax_image_numに格納する
    # 例: max_image_num = {'normal':2, 'speak':3, 'think':2}
    for status in app_status.Status:
        path = f'img/{character.value}/{status.value}'
        print(path)
        image_num =  sum(os.path.isfile(os.path.join(path,name)) for name in os.listdir(path))
        max_image_num[status.value] = image_num
    print(max_image_num)

def start():
    ft.app(target=main)