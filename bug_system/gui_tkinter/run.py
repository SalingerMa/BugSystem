# -*- coding: utf-8 -*-
from gui_tkinter import *
from gui_tkinter.t1 import GUI_Table

gui = GUI_Table()

gui.label1()
gui.label2()
gui.label3()
label1.grid(column=0, row=0, sticky='W', padx=8, pady=4)
label2.grid(column=0, row=2, sticky='W', padx=8, pady=4)
label3.grid(column=0, row=4, sticky='W', padx=8, pady=4)

gui.table1()
gui.table2()
gui.table3()
table1.grid(column=0, row=1, sticky='W', padx=8, pady=4, columnspan=3)
table2.grid(column=0, row=3, sticky='W', padx=8, pady=4, columnspan=3)
table3.grid(column=0, row=5, sticky='W', padx=8, pady=4, columnspan=3)




table_frame.grid(column=0, row=0, sticky='W', padx=8, pady=4)

window.mainloop()