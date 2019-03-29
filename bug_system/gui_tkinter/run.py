# -*- coding: utf-8 -*-
from gui_tkinter import *
from gui_tkinter.t1 import GUI_Table

gui = GUI_Table()
gui.label1()
gui.label2()
gui.label3()

gui.table1()
gui.table2()
gui.table3()

label1.grid(column=0, row=0, sticky='W', padx=4, pady=4)
label2.grid(column=0, row=2, sticky='W', padx=4, pady=4)
label3.grid(column=0, row=4, sticky='W', padx=4, pady=4)

table1.grid(column=0, row=1, sticky='W', padx=4, pady=8, columnspan=4)
table2.grid(column=0, row=3, sticky='W', padx=4, pady=8, columnspan=4)
table3.grid(column=0, row=5, sticky='W', padx=4, pady=8, columnspan=4)

gui.gui_bar()

tableChosen.grid(column=0, row=0, sticky='W', padx=4, pady=4)
barImageChosen.grid(column=1, row=0, sticky='W', padx=4, pady=4)
barImageButton.grid(column=2, row=0, sticky='W', padx=4, pady=4)

gui.init_del()

copyButton.grid(column=0, row=0, sticky='NW', padx=4, pady=4)
clean1Button.grid(column=1, row=0, sticky='NW', padx=4, pady=4)
clean2Button.grid(column=2, row=0, sticky='NW', padx=4, pady=4)

gui.init_analyze()

anaText.grid(column=2, row=0, sticky='NW', padx=4, pady=4)


table_frame.grid(column=0, row=0, sticky='W', padx=1, pady=2)
bar_frame.grid(column=1, row=0, sticky='W', padx=1, pady=2)

del_frame.grid(column=0, row=1, sticky='W', padx=1, pady=2)
analyze_frame.grid(column=1, row=1, sticky='W', padx=1, pady=2)

window.mainloop()