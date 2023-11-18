import tkinter
import tkinter.messagebox
import customtkinter
from cert_gen import create_self_signed_cert

# Настройки темы
customtkinter.set_appearance_mode("System")  # Темы: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Темы тоже, расцветка: blue (default), dark-blue, green

# Главное окно
app = customtkinter.CTk()  # создаем главное окно
app.geometry("400x240")  # Размер окна
app.resizable(False, False)  # Нельзя менять размеры окна
app.eval('tk::PlaceWindow . center')  # Размещаем главное окно по центру экрана (на самом деле не совсем)


def button_function():
    tkinter.messagebox.showinfo('Test', message='Test2')


# Кнопка
button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

# Левая навигационная панель, она же главная
navigation_panel = customtkinter.CTkFrame(app)
navigation_panel.pack(side=tkinter.LEFT)
navigation_panel.configure(width=100, height=240)

# Так надо =)
app.mainloop()
