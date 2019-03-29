# -*- coding: utf-8 -*-
from gui_tkinter import *
from gui_tkinter.create_table import Table
from common.config import TableName, TableHead, ImageName
from tkinter.ttk import Button
from tkinter import Text, StringVar, WORD, END
from gui_tkinter.gui_func import GUI_Func
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

columns = TableHead.column.value
base_path = str(os.getcwd()).replace('\\', '/') + '/images'
class GUI_Table:
    def __init__(self):
        self.t1 = Table(table1)
        self.t2 = Table(table2)
        self.t3 = Table(table3)
        self.barChosen = StringVar()
        self.tbChosen = StringVar()

    # table_frame
    def label1(self):
        label1.config(text=TableName.table1.value)
    def label2(self):
        label2.config(text=TableName.table2.value)
    def label3(self):
        label3.config(text=TableName.table3.value)

    def table1(self):
        self.t1.setTableHead(columns)
        GUI_Func.insert_table_data(self.t1, TableName.table1.value)

        table1.bind('<Double-1>', self.table1_set_cell_value)  # 双击左键进入编辑
    def table2(self):
        self.t2.setTableHead(columns)
        GUI_Func.insert_table_data(self.t2, TableName.table2.value)
        table2.bind('<Double-1>', self.table2_set_cell_value)  # 双击左键进入编辑
    def table3(self):
        self.t3.setTableHead(columns)
        GUI_Func.insert_table_data(self.t3, TableName.table3.value)
        table3.bind('<Double-1>', self.table3_set_cell_value)  # 双击左键进入编辑

    def table1_set_cell_value(self, event):  # 双击进入编辑状态
        for item in table1.selection():  # item = I001
            item_text = table1.item(item, "values")
            # print(item_text)  # 输出所选行的值
            # print(table1.selection())
        column = table1.identify_column(event.x)  # 列
        row = table1.identify_row(event.y)  # 行
        cn = int(str(column).replace('#', '')) - 1
        rn = int(str(row).replace('I', ''), 16) - 1
        entryedit = Text(table_frame, width=20, height=1)
        entryedit.grid(column=1, row=0, sticky='E', padx=8, pady=4)

        okb = Button(table_frame, text='OK', width=4, command=lambda: self.saveedit1(item, column, entryedit, okb, cn, rn))
        okb.grid(column=2, row=0, sticky='W', padx=8, pady=4)

    def table2_set_cell_value(self, event):  # 双击进入编辑状态
        for item in table2.selection():  # item = I001
            item_text = table2.item(item, "values")
            # print(item_text)  # 输出所选行的值
            # print(table2.selection())
        column = table2.identify_column(event.x)  # 列
        row = table2.identify_row(event.y)  # 行
        cn = int(str(column).replace('#', '')) - 1
        rn = int(str(row).replace('I', ''), 16) - 1
        entryedit = Text(table_frame, width=20, height=1)
        entryedit.grid(column=1, row=2, sticky='E', padx=8, pady=4)

        okb = Button(table_frame, text='OK', width=4, command=lambda: self.saveedit2(item, column, entryedit, okb, cn, rn))
        okb.grid(column=2, row=2, sticky='W', padx=8, pady=4)

    def table3_set_cell_value(self, event):  # 双击进入编辑状态
        for item in table3.selection():  # item = I001
            item_text = table3.item(item, "values")
            # print(item_text)  # 输出所选行的值
            # print(table2.selection())
        column = table3.identify_column(event.x)  # 列
        row = table3.identify_row(event.y)  # 行
        cn = int(str(column).replace('#', '')) - 1
        rn = int(str(row).replace('I', ''), 16) - 1
        entryedit = Text(table_frame, width=20, height=1)
        entryedit.grid(column=1, row=4, sticky='E', padx=8, pady=4)

        okb = Button(table_frame, text='OK', width=4, command=lambda: self.saveedit3(item, column, entryedit, okb, cn, rn))
        okb.grid(column=2, row=4, sticky='W', padx=8, pady=4)

    def saveedit1(self, item, column, entryedit, okb, cn, rn):
        try:
            if rn == 4 or cn >= 6:
                return None
            while True:
                if rn > 4:
                    rn -= 5
                else:
                    break
            value = entryedit.get(0.0, "end")
            GUI_Func.update_table(TableName.table1.value, rn, cn, int(value))

            table1.set(item, column=column, value=value)

            GUI_Func.insert_table_data(self.t1, TableName.table1.value)
            self.init_analyze()
        except:
            pass
        finally:
            entryedit.destroy()
            okb.destroy()

    def saveedit2(self, item, column, entryedit, okb, cn, rn):
        try:
            if rn == 4 or cn >= 6:
                return None
            while True:
                if rn > 4:
                    rn -= 5
                else:
                    break
            value = entryedit.get(0.0, "end")
            GUI_Func.update_table(TableName.table2.value, rn, cn, int(value))

            table2.set(item, column=column, value=value)

            GUI_Func.insert_table_data(self.t2, TableName.table2.value)
            self.init_analyze()
        except:
            entryedit.destroy()
            okb.destroy()

    def saveedit3(self, item, column, entryedit, okb, cn, rn):
        try:
            if rn == 4 or cn >= 6:
                return None
            while True:
                if rn > 4:
                    rn -= 5
                else:
                    break
            value = entryedit.get(0.0, "end")
            GUI_Func.update_table(TableName.table3.value, rn, cn, int(value))

            table3.set(item, column=column, value=value)

            GUI_Func.insert_table_data(self.t3, TableName.table3.value)
            self.init_analyze()
        except:
            entryedit.destroy()
            okb.destroy()

    # bar frame
    def gui_bar(self):
        tableChosen.config(width=25, textvariable=self.tbChosen)
        tablelist = ImageName.tablelist.value
        tableChosen['values'] = tablelist
        self.tbChosen.set(tablelist[0])

        barImageChosen.config(width=16, textvariable=self.barChosen)
        imglist = ImageName.imglist.value
        barImageChosen['values'] = imglist
        self.barChosen.set(imglist[0])

        barImageButton.config(text='OK', command=self.init_bar)

        self.init_bar()

    def init_bar(self):
        tbvalue = self.tbChosen.get()
        barvalue = self.barChosen.get()

        barvalue1, barvalue2 = barvalue.split('-')
        img_figure = GUI_Func.get_image_figure(tbvalue, barvalue1, barvalue2)

        self.canvas = FigureCanvasTkAgg(img_figure, bar_frame)
        self.canvas.draw()
        # self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.canvas.get_tk_widget().grid(column=0, row=1, sticky='W', padx=4, pady=4, columnspan=3)

    def copy_table(self):
        table2_data = GUI_Func.get_table_data(TableName.table2.value)
        for bug, value in table2_data.items():
            for i in range(len(value['data'])):
                row_num = TableHead.row.value.index(bug)
                GUI_Func.update_table(TableName.table3.value, row_num, i + 1, value['data'][i])
        GUI_Func.insert_table_data(self.t3, TableName.table2.value)
        self.init_analyze()
    def clean_table(self, tableName):
        for i in range(5):
            for j in range(6):
                GUI_Func.update_table(tableName, i, j+1, 0)
        if tableName == TableName.table1.value:
            GUI_Func.insert_table_data(self.t1, TableName.table1.value)
        elif tableName == TableName.table2.value:
            GUI_Func.insert_table_data(self.t2, TableName.table2.value)
        self.init_analyze()

    def init_del(self):
        copyButton.config(text="复制表2到表3", command=self.copy_table)
        clean1Button.config(text='清空表1', command=lambda: self.clean_table(TableName.table1.value))
        clean2Button.config(text='清空表2', command=lambda: self.clean_table(TableName.table2.value))

    # analyze_frame
    def init_analyze(self):
        anaText.config(width=73, height=6, wrap=WORD)
        ana_data = GUI_Func.get_analyze_data()
        self.anaText_clean()
        anaText.config(state='normal')
        for data in ana_data:
            self.anaText_insert(data)
        anaText.config(state='disabled')

    def anaText_insert(self, text):
        # anaText.config(state='normal')
        anaText.insert('end', text + "\n")
        # anaText.config(state='disabled')
        anaText.see(END)
        anaText.update()

    def anaText_clean(self):
        anaText.config(state='normal')
        anaText.delete('1.0', 'end')
        anaText.config(state='disabled')