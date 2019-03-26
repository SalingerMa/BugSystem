# -*- coding: utf-8 -*-
from common.mysqler import SQL
from common.config import TableHead
class Common:
    @classmethod
    def get_table_data(cls, table):
        """
        :param table:
        :return:{'Minor': [3, 0, 4, 1, 0], 'Bloker': [2, 10, 2, 1, 0], 'Major': [0, 15, 6, 0, 3], 'Critical': [3, 2, 1, 0, 3]}
        """
        data = SQL.select(table)
        table_data = {}
        for item in data:
            table_data[item[0]] = list(item[1:])
        return table_data

    @classmethod
    def get_table_column(cls, table):
        """
        :param table:
        :return: ['bug_id', 'AND', 'IOS', 'H5', 'SER', 'PRO']
        """
        data = SQL.select_column(table)
        columns = [item[0] for item in data]
        if 'BUG' in columns:
            columns.remove('BUG')
        return columns

    @classmethod
    def update_table_value(cls, table, x, y, value):

        key = TableHead.column.value[y]
        bug = TableHead.row.value[x]
        SQL.update_value(table, key, value, bug)

if __name__ == '__main__':
    a = Common.update_table_value('submit_bug_of_this_week', 2, 3, 10)
    print(a)
