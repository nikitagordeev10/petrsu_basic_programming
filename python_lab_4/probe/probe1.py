import tkinter as tk
window = tk.Tk()

greeting1 = tk.Label(text="Привет, Tkinter!")
greeting2 = tk.Button(text="Привет, Tkinter!")
greeting3 = tk.Entry(text="Привет, Tkinter!")
greeting4 = tk.Text()
greeting5 = tk.Frame()

greeting1.pack()
greeting2.pack()
greeting3.pack()
greeting4.pack()
greeting5.pack()

window.mainloop()