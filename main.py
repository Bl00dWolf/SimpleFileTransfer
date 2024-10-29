import flet as ft
from flet_core import RouteChangeEvent


def main(page: ft.Page) -> None:
    page.title = 'Simple File Transfer'
    page.window.alignment = ft.Alignment(0, 0)
    page.window.height = 700
    page.window.width = 500

    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER


    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.FILE_UPLOAD, label="Отправка"),
            ft.NavigationBarDestination(icon=ft.icons.FILE_DOWNLOAD, label="Получение"),
            ft.NavigationBarDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon=ft.icons.SETTINGS,
                label="Настройки",
            ),
        ]
    )
    page.add(ft.Text("Body!"))

ft.app(target=main)
