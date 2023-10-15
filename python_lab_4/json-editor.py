# Библиотеки
import json
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
import urllib.request
import tkinter.simpledialog as tkSimpleDialog


# Backend
# Графические окна "Файл"
# Открыть с этого компьютера
def open_from_computer():
    try:
        file_name = fd.askopenfilename()
        f = open(file_name)
    except:
        pass
    else:
        data = f.read()
        text_box.delete('1.0', 'end')
        text_box.insert('1.0', data)
        f.close()


# Открыть по URL
def open_from_url():
    try:
        url = tkSimpleDialog.askstring("Открыть по URL", "Введите электронный адрес - URL:")
        data = urllib.request.urlopen(url)
    except:
        messagebox.showerror(title="Ошибка", message="Введён не верный URL. Попробуйте ещё раз.")
    else:
        data = data.read().decode('utf-8')
        text_box.delete('1.0', 'end')
        text_box.insert('1.0', data)


# Сохранить на этот компьютер
def is_json(data):
    try:
        json.loads(data)
    except ValueError:
        return False
    return True


def save_to_computer():
    if is_json(text_box.get(1.0, END)):
        file = fd.asksaveasfile(mode='w', defaultextension='.json', filetypes=[("json files", '*.json')])
        file.write(text_box.get(1.0, END))
    else:
        messagebox.showerror(title="Сохранить на этот компьютер", message="Невозможно сохранить, в JSON коде ошибки")


# Графические окна "Правка"
# Графические окна "Проверка корректности"
def syntax_check():
    if is_json(text_box.get(1.0, END)):
        messagebox.showinfo(title="Проверка корректности", message="Всё правильно")
    else:
        messagebox.showerror(title="Проверка корректности", message="Есть ошибки")


# Графические окна "Справка"
# Графические окна "Руководство пользователя Редактор JSON"
def user_guide_json_editor():
    messagebox.showinfo('Руководство пользователя Редактор JSON',
                        'Внимание! При открытии инструкции Ваш код будет удалён!')
    file_name = 'info/user_guide_json_editor.txt'
    f = open(file_name)
    data = f.read()
    text_box.delete('1.0', 'end')
    text_box.insert('1.0', data)
    f.close()


# Графические окна "Формат файлов JSON"
def json_file_format():
    messagebox.showinfo('Формат файлов JSON', 'Внимание! При открытии инструкции Ваш код будет удалён!')
    file_name = 'info/json_file_format.txt'
    f = open(file_name)
    data = f.read()
    text_box.delete('1.0', 'end')
    text_box.insert('1.0', data)
    f.close()


# Frontend
# Параметры окна программы
window = Tk()
window.title("Редактор JSON")
window.geometry('900x500')

# Пункты меню
# Инициализация
menu = Menu(window)
file = Menu(menu, tearoff=0)
verify = Menu(menu, tearoff=0)
info = Menu(menu, tearoff=0)

# Выпадающие списки
menu.add_cascade(label='Файл', menu=file)
file.add_command(label='Открыть с этого компьютера', command=open_from_computer)
file.add_command(label='Открыть по URL', command=open_from_url)
file.add_separator()
file.add_command(label='Сохранить на этот компьютер', command=save_to_computer)
file.add_separator()
file.add_command(label='Закрыть файл', command=lambda: text_box.delete('1.0', 'end'))
file.add_command(label='Выход из программы', command=lambda: exit(0))

menu.add_cascade(label='Правка', menu=verify)
verify.add_command(label='Проверка корректности', command=syntax_check)

menu.add_cascade(label='Справка', menu=info)
info.add_command(label='Руководство пользователя Редактор JSON', command=user_guide_json_editor)
info.add_separator()
info.add_command(label='Формат файлов JSON', command=json_file_format)
window.config(menu=menu)

# Текстовая область
text_box = Text(window)
scrollbar = Scrollbar(window)

text_box['yscrollcommand'] = scrollbar.set
text_box.pack(side='left', fill='both', expand=1)
scrollbar.pack(side='right', fill='y')

window.mainloop()
