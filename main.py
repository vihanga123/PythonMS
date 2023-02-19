import tkinter
from tkinter import *

top=Tk()
top.title("Student LMS")
top.geometry("400x200")
heading = tkinter.Label(text="This is a test", background="#34A2FE",foreground="white")
heading.grid(row=0,column=2)

label=tkinter.Label(text="Insert Name: ")
label.grid(row=2,column=1)
entry=tkinter.Entry()
entry.grid(row=2,column=2)

label=tkinter.Label(text="Insert Password: ")
label.grid(row=4,column=1)
entry=tkinter.Entry()
entry.grid(row=4,column=2)

button = tkinter.Button(text='test')
button.grid(row=5,column=1)
button2 = tkinter.Button(text='test')
button2.grid(row=5,column=2)

top.mainloop()
