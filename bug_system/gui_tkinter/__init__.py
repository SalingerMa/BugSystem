# -*- coding: utf-8 -*-
from tkinter import Tk, Canvas, scrolledtext
from tkinter.ttk import Treeview, Frame, Label, Combobox, Button

window = Tk()
window.title('Bug System')
window['bg'] = '#FFDEAD'
table_frame = Frame(window)
bar_frame = Frame(window)
analyze_frame = Frame(window)
del_frame = Frame(window)
table1 = Treeview(table_frame)
table2 = Treeview(table_frame)
table3 = Treeview(table_frame)

label1 = Label(table_frame)
label2 = Label(table_frame)
label3 = Label(table_frame)

tableChosen = Combobox(bar_frame)
barImageChosen = Combobox(bar_frame)
barImageButton = Button(bar_frame)
barcanves = Canvas()

copyButton = Button(del_frame)
clean1Button = Button(del_frame)
clean2Button = Button(del_frame)

anaText = scrolledtext.ScrolledText(analyze_frame)

