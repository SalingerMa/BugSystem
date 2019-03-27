# -*- coding: utf-8 -*-
from gui_tkinter import *
from gui_tkinter.create_table import Table
from common.config import TableName, TableHead

from gui_tkinter.gui_func import GUI_Func

columns = TableHead.column.value

class GUI_Table:
    def __init__(self):
        self.t1 = Table(table1)
        self.t2 = Table(table2)
        self.t3 = Table(table3)

    def label1(self):
        label1.config(text="表1")
    def label2(self):
        label2.config(text="表2")
    def label3(self):
        label3.config(text="表3")

    def table1(self):
        self.t1.setTableHead(columns)
        GUI_Func.insert_table_data(self.t1, TableName.table1.value)

        table1.bind('<Double-1>', GUI_Func.table1_set_cell_value)  # 双击左键进入编辑
        table1.bind('<Double-1>', GUI_Func.table1_set_cell_value)  # 双击左键进入编辑

    def table2(self):
        self.t2.setTableHead(columns)
        GUI_Func.insert_table_data(self.t2, TableName.table2.value)

    def table3(self):
        self.t3.setTableHead(columns)
        GUI_Func.insert_table_data(self.t3, TableName.table3.value)



