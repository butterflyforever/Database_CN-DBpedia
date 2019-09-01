# !/usr/bin/python
# -*- coding: UTF-8 -*-
import sys 
sys.path.append("/Users/liyang/Desktop/Course/Database/Project/code/nlp/") 
from query_process import *
from tkinter import *
import tkinter
#import tkMessageBox

window = tkinter.Tk()
#window.geometry('1000x618')
window.title('DataBase')
window.resizable(0,0)
Label(window, text="Input", font="Times 15 bold italic").grid(row=0)
Label(window, text="Output", font="Times 15 bold italic").grid(row=1)
entry1 = Entry(window, width = 50, font="Helvetica 20 bold")
entry2 = Entry(window, width = 50, font="Helvetica 20 bold")
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

def search():
    return 'null'

def database():
    entry2['state'] = 'normal'
    entry2.delete(0, END)
    input_blank  = entry1.get()
    result = str(analysis(input_blank))#input + search()
    entry2.insert(10, result)
    entry2['state'] = 'readonly'


Button(window, text='Quit', command=window.quit, font="Times 15 bold italic", fg='red').grid(row=2, column=0, sticky=W, padx=5, pady=5)
Button(window, text='Search', command=database, relief = 'solid', font="Times 15 bold italic", fg='blue').grid(row=2, column=1, sticky=W, padx=5, pady=5)
##flat, groove, raised, ridge, solid, or sunken
window.mainloop()