# -*- coding: utf-8 -*-
from common.function import Common
from common.config import TableHead
import os

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
    def update_table(cls, table_name, row, col, value):
        bug = TableHead.row.value[row]
        key = TableHead.column.value[col]
        if key == 'ALL' or bug == 'ALL':
            return None
        Common.update_table_value(table_name, key, bug, value)

