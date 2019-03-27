# -*- coding: utf-8 -*-
from gui_tkinter import table1, table2, table3
from  gui_tkinter.gui_func import GUI_Func

class Table():

    def __init__(self, table):
        self.table = table

    def setTableHead(self, columns):
        self.table.config(height=5, show="headings", columns=columns)
        for col in columns:
            self.table.column(col, width=80, anchor='center')
            self.table.heading(col, text=col)

    def insertOneRow(self, index, values):
        self.table.insert('', index, values=values)

    def insertAllTable(self, data):
        for i in range(len(data)):
            self.insertOneRow(i, data[i])