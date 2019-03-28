# -*- coding: utf-8 -*-
from tkinter import Tk, Canvas
from tkinter.ttk import Treeview, Frame, Label, Combobox, Button

window = Tk()
window.title('Bug System')
window['bg'] = '#FFDEAD'
table_frame = Frame(window)
bar_frame = Frame(window)
pie_frame = Frame(window)

table1 = Treeview(table_frame)
table2 = Treeview(table_frame)
table3 = Treeview(table_frame)

label1 = Label(table_frame)
label2 = Label(table_frame)
label3 = Label(table_frame)

barImageChosen = Combobox(bar_frame)
barImageButton = Button(bar_frame)
barcanves = Canvas()



