# -*- coding: utf-8 -*-
import pymysql

db_host = 'localhost'
db_user = 'root'
db_pwd = '123456'
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
        sql = "UPDATE `%s` SET `%s`=%s WHERE `BUG`='%s'" % (table, key, value, bug)
        cursor.execute(sql)
        db.commit()
        return cursor.fetchall()

if __name__ == '__main__':
    a = SQL.update_value('submit_bug_of_this_week', 'AND', 10, 'Major')
    print(a)
