# -*- coding: utf-8 -*-
import pymysql
from pymysql.err import ProgrammingError, InternalError
db_host = 'localhost'
db_user = 'root'
db_pwd = 'xls1208'
db_data = 'bug_system'

db = pymysql.connect(db_host, db_user, db_pwd, db_data, charset="utf8")
cursor = db.cursor()

class SQL:

    @classmethod
    def select(cls, table):
        sql = "SELECT * FROM %s" % table
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def select_column(cls, table):
        sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = %s"
        cursor.execute(sql, table)
        return cursor.fetchall()

    @classmethod
    def update_value(cls, table, key, value, bug):
        sql = "UPDATE `%s` SET `%s`=%s WHERE `BUG`='%s'" % (table, key, int(value), bug)
        cursor.execute(sql)
        db.commit()
        return cursor.fetchall()
    @classmethod
    def insert_one(cls, table, data, duplicate_update=False):
        """
        插入一组数据
        :param table: 表名
        :param data: 插入的数据（以字典的形式传入）
        :param duplicate_update: 是否查重更新：若主键重复，则将插入数据变为更新数据
        :return: 空
        """
        key = ', '.join(data.keys())
        value = ', '.join(['%s'] * len(data.keys()))

        sql = "INSERT INTO {table}({key}) VALUES({value})".format(table=table, key=key, value=value)
        sql_value = tuple(data.values())

        if duplicate_update:
            update = ', '.join(['{}=%s'.format(i) for i in data.keys()])
            sql += ' ON DUPLICATE KEY UPDATE {update}'.format(update=update)
            sql_value = sql_value * 2
        try:
            cursor.execute(sql, sql_value)
            db.commit()
        except (ProgrammingError, InternalError) as e:
            print("插入数据错误:", e)
            return None




if __name__ == '__main__':
    a = SQL.update_value('submit_bug_of_this_week', 'AND', 10, 'Bloker')
    print(a)
