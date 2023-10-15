from tkinter import *
from tkinter import filedialog as fd
import tkinter.simpledialog as tkSimpleDialog
import tkinter.messagebox as message_box
import urllib.request
import json

def insert_text():
    try:
        file_name = fd.askopenfilename()
        f = open(file_name)
    except:
        message_box.showerror(title="Error", message="Wrong url")
    else:
        s = f.read()
        text_box.insert(1.0, s)
        f.close()

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

root = Tk()
text_box = Text(width=50, height=25)
text_box.grid(columnspan=2)
b1 = Button(text="Открыть", command=insert_text())
b1.grid(row=1, sticky=E)
root.mainloop()
