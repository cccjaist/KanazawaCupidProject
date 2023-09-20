import flet as ft
flag = False

global my_status

async def main(page: ft.Page):
    img = ft.Image(
        src = f"test.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )
    
    async def change_image(e):
        my_status
        img_name = "test.png" if flag else "test2.png"

        img.src = img_name
        await page.update_async()

    page.title = "金沢キューピッド"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50
    await page.update_async()

    question = ft.TextField(label="会話内容")
    send_button = ft.ElevatedButton("君はどう思う？", on_click=change_image)

    await page.add_async(img, question, send_button)

def start():
    ft.app(target=main)