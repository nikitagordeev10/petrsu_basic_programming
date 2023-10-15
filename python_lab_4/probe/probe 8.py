# Построение интерфейсов. Графическое приложение, удовлетворяющее следующим требованиям:
# Пользователь может указать ссылку на файл JSON (пример).
# Приложение загружает файл, отображает его в удобочитаемом формате, позволяет отредактировать.
# Пользователь может сохранить отредактированный файл в выбранную директорию файловой системы.
# Обязательна проверка корректности сохраняемого файла

from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import filedialog
from tkinter import Menu
from os import path
from tkinter import *
from tkinter import filedialog
import tkinter.simpledialog as tkSimpleDialog
import tkinter.messagebox as message_box
import urllib.request
import json


def is_JSON(data):
    try:
        json.loads(data)
    except ValueError as e:
        return False
    return True


def load():
    try:
        url = tkSimpleDialog.askstring("", "Enter a url:")
        data = urllib.request.urlopen(url)
    except:
        message_box.showerror(title="Error", message="Wrong url")
    else:
        data = data.read().decode('utf-8')
        data = "".join(filter(str.strip, data.split('\r')))
        text_box.delete('1.0', 'end')
        text_box.insert('1.0', data)


def check():
    if is_JSON(text_box.get(1.0, END)):
        message_box.showwarning(title="Syntax checker", message="All good")
    else:
        message_box.showerror(title="Syntax checker", message="Invalid syntax")


def save_as():
    if is_JSON(text_box.get(1.0, END)):
        file = filedialog.asksaveasfile(mode='w', defaultextension='.json', filetypes=[("json files", '*.json')])
        file.write(text_box.get(1.0, END))
    else:
        message_box.showerror(title="Syntax checker", message="Invalid syntax!")

window = Tk()
window.geometry('900x500')
window.title("Редактор JSON")

main_menu = Menu(window)
window.config(menu=main_menu)

file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="по URL", command=load)
file_menu.add_command(label="c компьютера", command=load)
file_menu.add_command(label="Check", command=check)
file_menu.add_separator()
file_menu.add_command(label="Save as", command=save_as)
file_menu.add_command(label="Close file", command=lambda: text_box.delete('1.0', 'end'))
file_menu.add_command(label="Exit", command=lambda: exit(0))
text_box = Text(window, font='Calibri 9', wrap='word')


scrollbar = Scrollbar(window)

text_box['yscrollcommand'] = scrollbar.set

text_box.pack(side='left', fill='both', expand=1)
scrollbar.pack(side='right', fill='y')

main_menu.add_cascade(label="Загрузка", menu=file_menu)
main_menu.add_cascade(label="Проверка", menu=file_menu)
main_menu.add_cascade(label="Сохраниние", menu=file_menu)
main_menu.add_cascade(label="Закрытие", menu=file_menu)
main_menu.add_cascade(label="Выход", menu=file_menu)

window.mainloop()  # Бесконечный цикл окна
