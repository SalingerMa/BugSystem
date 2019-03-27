# -*- coding: utf-8 -*-
from common.function import Common
from common.config import TableName, TableHead
from tkinter.ttk import Button
from tkinter import Text
from gui_tkinter import table1, table2, table3, table_frame

class GUI_Func:
    @classmethod
    def parse_data(cls, data):
        sum_row = [0] * len(data[0])

        for item in range(len(data)):
            data[item].append(sum(data[item][1:]))
            sum_row = [sum_row[i] + data[item][1:][i] for i in range(len(data[item][1:]))]

        sum_row.insert(0, 'ALL')
        data.append(sum_row)
        return data

    @classmethod
    def insert_table_data(cls, table, table_name):
        table_data = cls.parse_data(Common.get_table_data(table_name))
        table.insertAllTable(table_data)
    @classmethod
    def table1_set_cell_value(cls, event):  # 双击进入编辑状态
        for item in table1.selection():  # item = I001
            item_text = table1.item(item, "values")
            print(item_text)  # 输出所选行的值
        column = table1.identify_column(event.x)  # 列
        row = table1.identify_row(event.y)  # 行
        cn = int(str(column).replace('#', ''))
        rn = int(str(row).replace('I', ''))
        entryedit = Text(table_frame, width=20, height=1)
        entryedit.grid(column=1, row=0, sticky='E', padx=8, pady=4)

        def saveedit():
            table1.set(item, column=column, value=entryedit.get(0.0, "end"))
            entryedit.destroy()
            okb.destroy()

        okb = Button(table_frame, text='OK', width=4, command=saveedit)
        okb.grid(column=2, row=0, sticky='W', padx=8, pady=4)
