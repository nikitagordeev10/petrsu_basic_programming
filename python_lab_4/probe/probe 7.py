from tkinter import *
from tkinter import filedialog
import tkinter.simpledialog as tkSimpleDialog
import tkinter.messagebox as message_box
import urllib.request
import json

#
# Проверка на json файл
#
def is_JSON(data):
    try:
        json.loads(data)
    except ValueError as e:
        return False
    return True

#
# Загрузка JSON файла из интернета по url
#
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

#
# Проверка синтаксиса
# Выводит сообщение
#
def check():
    if is_JSON(text_box.get(1.0, END)):
        message_box.showwarning(title="Syntax checker",
                                message="All good")
    else:
        message_box.showerror(title="Syntax checker",
                              message="Invalid syntax")
        
#
# Сохранение файла на диске
#
def save_as():
    if is_JSON(text_box.get(1.0, END)):
        file = filedialog.asksaveasfile(mode='w', defaultextension='.json', filetypes=[("json files", '*.json')])
        file.write(text_box.get(1.0, END))
    else:
        message_box.showerror(title="Syntax checker", message="Invalid syntax!")
        
window = Tk()                                   # Запускаем Tkinter
window.geometry('800x600')                      # Задаём размеры
window.title("JSON Editor")                     # Даём название окну

main_menu = Menu(window)                        # Создаём меню вверху
window.config(menu=main_menu)                   #

file_menu = Menu(main_menu, tearoff=0)          #
file_menu.add_command(label="Load",   # Дрбавляем кнопку
                     command=load)         # загрузки JSON

file_menu.add_command(label="Check",     # Добавляем кнопку
                     command=check)      # проверки синтаксиса

file_menu.add_separator()                       # Добавляем один разделитель

file_menu.add_command(label="Save as",     # Добалвяем кнопку
                     command=save_as)      # сохранения файла на диске

file_menu.add_command(label="Close file",       # Добавляем возможность закрыть файл
                     command= lambda: text_box.delete('1.0', 'end'))

file_menu.add_command(label="Exit",             # Добавляем возможность выйти из редактора
                     command= lambda: exit(0))

text_box = Text(window,
               font='Calibri 9',
               wrap='word')

scrollbar = Scrollbar(window)

text_box['yscrollcommand'] = scrollbar.set

text_box.pack(side='left',
             fill='both',
             expand=1)

scrollbar.pack(side='right',
               fill='y')

main_menu.add_cascade(label="File",
                     menu=file_menu)

window.mainloop()
