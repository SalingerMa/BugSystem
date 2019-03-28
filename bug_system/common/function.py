# -*- coding: utf-8 -*-
from common.mysqler import SQL
from common.config import TableHead
class Common:
    @classmethod
    def get_table_data(cls, tableName):
        """
        :param table:
        :return:{'Minor': [3, 0, 4, 1, 0], 'Bloker': [2, 10, 2, 1, 0], 'Major': [0, 15, 6, 0, 3], 'Critical': [3, 2, 1, 0, 3]}
        """
        data = SQL.select(tableName)
        return [list(item) for item in data]

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
    def update_table_value(cls, table, key, bug, value):
        SQL.update_value(table, key, value, bug)

if __name__ == '__main__':
    a = Common.update_table_value('submit_bug_of_this_week', 'AND', 'Bloker', 20)
    print(a)
