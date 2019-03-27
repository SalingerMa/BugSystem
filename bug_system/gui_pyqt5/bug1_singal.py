# -*- coding: utf-8 -*-
from gui_pyqt5.bug1_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from common.function import Common
from common.config import TableName, RGB, Name, TableHead
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.init_table(table_obj=self.submit_table, table_name=TableName.table1.value)
        self.init_table(table_obj=self.rest_table, table_name=TableName.table2.value)
        self.init_table(table_obj=self.old_rest_table, table_name=TableName.table3.value)

        self.submit_table.cellChanged.connect(self.on_table_show)
        self.refresh_button.clicked.connect(self.on_table_refresh)

    def insert_value(self, table_obj, x, y, value):

        sum_all = QtWidgets.QTableWidgetItem(str(value))
        sum_all.setBackground(QColor(RGB.color2.value))
        sum_all.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        table_obj.setItem(x, y, sum_all)

    def calculator_all(self, table_obj, col_, row_):
        col_ = int(col_)
        row_ = int(row_)
        for j in range(row_ - 1):
            item = 0
            for i in range(col_):
                if i == col_ - 1:
                    self.insert_value(table_obj, j, i, item)
                else:
                    item += int(table_obj.item(j, i).text())
        for n in range(col_):
            item = 0
            for m in range(row_):
                if m == row_ - 1:
                    self.insert_value(table_obj, m, n, item)
                else:
                    item += int(table_obj.item(m, n).text())

    def init_table(self, table_obj, table_name):
        columns = TableHead.column.value
        rows = TableHead.row.value
        columns.append('ALL')
        rows.append('ALL')
        col_count = len(columns)
        row_count = len(rows)

        table_obj.setColumnCount(col_count)
        table_obj.setRowCount(row_count)
        table_obj.setHorizontalHeaderLabels(columns)
        table_obj.setVerticalHeaderLabels(rows)

        table_data = Common.get_table_data(table_name)
        cell_data = 0
        for i in range(row_count - 1):
            for j in range(col_count - 1):
                if i == 0:
                    cell_data = table_data[Name.grade1.value][j]
                elif i == 1:
                    cell_data = table_data[Name.grade2.value][j]
                elif i == 2:
                    cell_data = table_data[Name.grade3.value][j]
                elif i == 3:
                    cell_data = table_data[Name.grade4.value][j]

                item = QtWidgets.QTableWidgetItem(str(cell_data))

                item.setBackground(QColor(RGB.color1.value))
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                table_obj.setItem(i, j, item)

        # self.calculator_all(table_obj, col_count, row_count)


    def on_table_show(self, p_int, p_int_1):
        item = self.submit_table.item(p_int, p_int_1).text()
        Common.update_table_value(TableName.table1.value, p_int, p_int_1, item)
        # self.calculator_all(self.submit_table, self.submit_table.columnCount(), self.submit_table.rowCount())
        self.init_table(self.submit_table, TableName.table1.value)
    def on_table_refresh(self):
        self.calculator_all(self.submit_table, self.submit_table.columnCount(), self.submit_table.rowCount())

    # def onChinaClicked(self):
    #     self.Title.setText("Hello China")
    # def onlineEditTextChanged(self, p_str):
    #     self.Title.setText(p_str)