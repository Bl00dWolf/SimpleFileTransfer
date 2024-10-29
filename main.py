import json

import flet as ft
import os

settings = {'app_theme': 'dark', 'app_height': 700, 'app_width': 500}


def settings_file() -> None:
    new_params = False
    if os.path.exists('settings.json'):
        with open('settings.json', 'r', encoding='utf-8') as file:
            global settings
            settings_temp = json.load(file)

            for key, value in settings.items():
                if key not in settings_temp.keys():
                    settings_temp[key] = value
                    new_params = True

            settings = settings_temp

        if new_params:
            with open('settings.json', 'w', encoding='utf-8') as file:
                json.dump(settings_temp, file, indent=4)

    else:
        with open('settings.json', 'w', encoding='utf-8') as file:
            json.dump(settings, file, ensure_ascii=True, indent=4)


def main(page: ft.Page) -> None:
    page.title = 'Simple File Transfer'
    page.window.alignment = ft.Alignment(0, 0)
    page.window.height = settings['app_height']
    page.window.width = settings['app_width']

    page.theme_mode = settings['app_theme']
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


settings_file()
ft.app(target=main)
