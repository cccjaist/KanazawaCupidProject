import app_status
import os
import flet as ft

global character
global my_status

max_image_num = {}
now_image_num = 0

async def main(page: ft.Page):
    global now_image_num
    img_path, now_image_num = get_image(now_image_num)
    img = ft.Image(
        src = img_path,
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )
    
    async def change_image(e):
        global now_image_num
        img_path, now_image_num = get_image(now_image_num)
        img.src = img_path
        await page.update_async()

    page.title = "金沢キューピッド"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50
    await page.update_async()

    question = ft.TextField(label="会話内容")
    send_button = ft.ElevatedButton("君はどう思う？", on_click=change_image)

    await page.add_async(img, question, send_button)

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