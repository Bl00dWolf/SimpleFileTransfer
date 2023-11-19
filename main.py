import tkinter
import tkinter.messagebox
import customtkinter
import settings


def main():
    # список всех созданных кнопок
    buttons_list = []

    # отключить текущую кнопку, включить все другие в навигационном меню
    def disable_button(button):
        cur_fg_color = button.cget('fg_color')
        # возвращаем все кнопки в исходное, рабочее состояние
        [(bt.configure(state=customtkinter.NORMAL, fg_color=cur_fg_color)) for bt in buttons_list]
        # отключаем текущую нажатую кнопку и подсвечиваем, что выбран этот пункт меню
        button.configure(state=customtkinter.DISABLED, fg_color='#3b9e0d', text_color_disabled='#f6f5fa')

    def settings_button_pressed(button):
        disable_button(button)

    # Настройки темы
    customtkinter.set_appearance_mode("System")  # Темы: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Темы тоже, расцветка: blue (default), dark-blue, green

    # Главное окно
    app = customtkinter.CTk()  # создаем главное окно
    app.title('Simple File Transfer')  # Заголовок окна
    app.iconbitmap('icon.ico')
    app.geometry("800x500")  # Размер окна
    app.resizable(False, False)  # Нельзя менять размеры окна
    app.eval('tk::PlaceWindow . center')  # Размещаем главное окно по центру экрана (на самом деле не совсем)

    # Левая навигационная панель, она же главная
    navigation_panel = customtkinter.CTkFrame(app)
    navigation_panel.pack(side=tkinter.LEFT)
    navigation_panel.configure(width=200, height=500)

    # Пункт меню, кнопка "Передача файлов"
    files_pg_button = customtkinter.CTkButton(master=navigation_panel, text='Передача файлов',
                                              command=lambda: settings_button_pressed(files_pg_button),
                                              font=('Bold', 20), bg_color='transparent')
    files_pg_button.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

    # Пункт меню, кнопка "Настройки"
    settings_pg_button = customtkinter.CTkButton(master=navigation_panel, text='Настройки',
                                                 command=lambda: settings_button_pressed(settings_pg_button),
                                                 font=('Bold', 20), bg_color='transparent')
    settings_pg_button.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

    buttons_list.extend([files_pg_button, settings_pg_button])

    # Так надо
    app.mainloop()


if __name__ == '__main__':
    main()
