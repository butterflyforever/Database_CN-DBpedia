# !/usr/bin/python
# -*- coding: UTF-8 -*-
import sys 
sys.path.append("/Users/liyang/Desktop/Course/Database/Project/code/nlp/") 
from query_process import *
from tkinter import *
import tkinter

window = tkinter.Tk()
#window.geometry('1000x618')
window.title('DataBase')
window.resizable(0,0)
Label(window, text="Input", font="Times 15 bold italic").grid(row=0)
Label(window, text="Output", font="Times 15 bold italic").grid(row=1)
entry1 = Text(window, width = 50, height=3, font="Helvetica 20 bold")#, bg='red')
text1 = Text(window, width = 50, height=20, font="Helvetica 20 bold", bg='#f0ffff')
entry1.grid(row=0, column=1)
text1.grid(row=1, column=1)

def database():
    text1['state'] = 'normal'
    text1.delete('1.0', END)
    input_blank  = entry1.get('1.0', END)
    result = str(analysis(input_blank))
    text1.insert(INSERT, result)
    text1['state'] = 'disabled'

Button(window, text='Quit', command=window.quit, font="Times 15 bold italic", fg='red').grid(row=2, column=0, sticky=W, padx=5, pady=5)
Button(window, text='Search', command=database, relief = 'solid', font="Times 15 bold italic", fg='blue').grid(row=2, column=1, sticky=W, padx=5, pady=5)
##flat, groove, raised, ridge, solid, or sunken
window.mainloop()