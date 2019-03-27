# -*- coding: utf-8 -*-
from tkinter import Tk
from tkinter.ttk import Treeview, Frame, Label

window = Tk()
window['bg'] = '#FFDEAD'
table_frame = Frame(window)

table1 = Treeview(table_frame)
table2 = Treeview(table_frame)
table3 = Treeview(table_frame)

label1 = Label(table_frame)
label2 = Label(table_frame)
label3 = Label(table_frame)