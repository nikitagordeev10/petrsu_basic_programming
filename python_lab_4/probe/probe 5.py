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

def clicked():
    # lbl.configure(text="Я же просил...")

    # res = "Привет {}".format(txt.get())
    # lbl.configure(text=res)

    # lbl.configure(text=selected.get())

    messagebox.showinfo('Заголовок', 'Текст')
    messagebox.showwarning('Заголовок', 'Текст')  # показывает предупреждающее сообщение
    messagebox.showerror('Заголовок', 'Текст')  # показывает сообщение об ошибке

    pass

window = Tk()
window.geometry('400x250')
window.title("Добро пожаловать в приложение PythonRu")

combo = Combobox(window)
chk = Checkbutton(window, text='Выбрать')

# lbl = Label(window, text="Привет", font=("Arial Bold", 12))
# lbl.grid(column=0, row=0)
#
# btn = Button(window, text="Клик!", bg="white", fg="black", command=clicked)
# btn.grid(column=2, row=0)
#
# txt = Entry(window, width=10) # state='disabled'
# txt.grid(column=1, row=0)
# txt.focus()

# combo['values'] = (1, 2, 3, 4, 5, "Текст")
# combo.current(1)  # установите вариант по умолчанию
# combo.grid(column=0, row=0)
# combo.get()

# chk_state = BooleanVar()
# chk_state.set(True)  # задайте проверку состояния чекбокса
# chk = Checkbutton(window, text='За Победу!', var=chk_state)
# chk.grid(column=0, row=0)

# chk_state = IntVar()
# chk_state.set(0) # False
# chk_state.set(1) # True
# chk = Checkbutton(window, text='За Победу!', var=chk_state)
# chk.grid(column=0, row=0)

# rad1 = Radiobutton(window,text='Первая', value=1, command=clicked_rad())
# rad2 = Radiobutton(window, text='Второй', value=2)
# rad3 = Radiobutton(window, text='Третий', value=3)
# rad1.grid(column=0, row=0)
# rad2.grid(column=1, row=0)
# rad3.grid(column=2, row=0)

# selected = IntVar()
# rad1 = Radiobutton(window, text='Первый', value=1, variable=selected)
# rad2 = Radiobutton(window, text='Второй', value=2, variable=selected)
# rad3 = Radiobutton(window, text='Третий', value=3, variable=selected)
# btn = Button(window, text="Клик", command=clicked)
# lbl = Label(window)
# rad1.grid(column=0, row=0)
# rad2.grid(column=1, row=0)
# rad3.grid(column=2, row=0)
# btn.grid(column=3, row=0)
# lbl.grid(column=0, row=1)
# window.mainloop()

# txt = scrolledtext.ScrolledText(window,width=40,height=10)
# txt.grid(column=0, row=0)
# txt.delete(1.0, END)  # мы передали координаты очистки
# txt.insert(INSERT, 'Текстовое поле')

# btn = Button(window, text='Клик', command=clicked)
# btn.grid(column=0, row=0)

# res = messagebox.askquestion('Заголовок', 'Текст')
# res = messagebox.askyesno('Заголовок', 'Текст')
# res = messagebox.askyesnocancel('Заголовок', 'Текст')
# res = messagebox.askokcancel('Заголовок', 'Текст')
# res = messagebox.askretrycancel('Заголовок', 'Текст')

# spin = Spinbox(window, from_=0, to=100, width=5)
# spin = Spinbox(window, values=(3, 8, 11), width=5)
# spin.grid(column=0, row=0)

# var = IntVar()
# var.set(36)
# spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
# spin.grid(column=0, row=0)

# bar = Progressbar(window, length=200)
# bar['value'] = 70
# bar.grid(column=0, row=0)

# style = ttk.Style()
# style.theme_use('default')
# style.configure("black.Horizontal.TProgressbar", background='black')
# bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
# bar['value'] = 70
# bar.grid(column=0, row=0)

# file = filedialog.askopenfilename()
# files = filedialog.askopenfilenames()
# file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
# dir = filedialog.askdirectory()
# file = filedialog.askopenfilename(initialdir= path.dirname(__file__))

# menu = Menu(window)
# new_item = Menu(menu, tearoff=0)
# new_item.add_command(label='Новый')
# # new_item.add_separator()
# new_item.add_command(label='Изменить')
# menu.add_cascade(label='Файл', menu=new_item)
# new_item.add_command(label='Новый', command=clicked)
# window.config(menu=menu)

# tab_control = ttk.Notebook(window)
# tab1 = ttk.Frame(tab_control)
# tab2 = ttk.Frame(tab_control)
# tab_control.add(tab1, text='Первая')
# tab_control.add(tab2, text='Вторая')
# lbl1 = Label(tab1, text= 'label1', padx=5, pady=5)
# lbl1.grid(column=0, row=0)
# lbl2 = Label(tab2, text='Вкладка 2')
# lbl2.grid(column=0, row=0)
# tab_control.pack(expand=1, fill='both')

window.mainloop()  # бесконечный цикл окна
