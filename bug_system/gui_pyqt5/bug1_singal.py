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

        self.submit_table.cellChanged.connect(self.on_table_show)

    def init_table(self, table_obj, table_name):
        table_data = Common.get_table_data(table_name)

        columns = Common.get_table_column(table_name)
        rows = []
        cols_all = [0, 0, 0, 0, 0]
        rows_all = []
        for key, value in table_data.items():
            rows.append(key)
            rows_all.append(sum(value))
            for i in range(len(cols_all)):
                cols_all[i] += value[i]
        bug_all = sum(rows_all) + sum(cols_all)

        columns.append('ALL')
        rows.append('ALL')

        col_count = len(columns)
        row_count = len(rows)

        table_obj.setColumnCount(col_count)
        table_obj.setRowCount(row_count)
        table_obj.setHorizontalHeaderLabels(columns)
        table_obj.setVerticalHeaderLabels(rows)

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
                else:
                    cell_data = 0
                item = QtWidgets.QTableWidgetItem(str(cell_data))

                item.setBackground(QColor(RGB.color1.value))
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                table_obj.setItem(i, j, item)

        for i in range(len(cols_all)):
            cell_data = cols_all[i]
            item = QtWidgets.QTableWidgetItem(str(cell_data))

            item.setBackground(QColor(RGB.color2.value))
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            table_obj.setItem(4, i, item)
            item.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable)

        for j in range(len(rows_all)):
            cell_data = rows_all[j]
            item = QtWidgets.QTableWidgetItem(str(cell_data))

            item.setBackground(QColor(RGB.color2.value))
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            table_obj.setItem(j, 5, item)
            item.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable)

        item = QtWidgets.QTableWidgetItem(str(bug_all))
        item.setBackground(QColor(RGB.color2.value))
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        table_obj.setItem(4, 5, item)
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable)

    def on_table_show(self, p_int, p_int_1):
        # print(p_int, p_int_1)
        item = self.submit_table.item(p_int, p_int_1).text()
        # print(item)
        Common.update_table_value(TableName.table1.value, p_int, p_int_1, item)
        self.refresh_sum_all(self.submit_table)
    def refresh_sum_all(self, table_obj):
        rows_all = []
        row_sum = 0
        for i in range(len(TableHead.column.value)):
            item = table_obj.item(0, i).text()




    # def onChinaClicked(self):
    #     self.Title.setText("Hello China")
    # def onlineEditTextChanged(self, p_str):
    #     self.Title.setText(p_str)