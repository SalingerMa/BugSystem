# -*- coding: utf-8 -*-
from common.function import Common
from common.config import TableHead, TableName, Name
from image.image import Image, Data
from tkinter.messagebox import showwarning
class GUI_Func:
    @classmethod
    def get_waring(cls):
        showwarning('警告', '不能修改统计值')

    @classmethod
    def get_table_data(cls, tableName):
        return Data.get_data(tableName)

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

    @classmethod
    def get_image_figure(cls, tbvalue,barvalue1, barvalue2):
        if tbvalue == 'resolved_bug_of_this_week':
            table_data = cls.get_resolved_data()
        else:
            table_data = Data.get_data(tbvalue)

        if barvalue1 == "Bar":
            if barvalue2 == 'ALL':
                sum_ = cls.get_table_sum(tbvalue)
                img_figure = cls.get_bar(table_data, title=tbvalue + ': ALL' + ' (Num: %s)' % sum_)
            elif barvalue2 == 'AND':
                img_figure = cls.get_bar_one(table_data, 0, title=tbvalue + ': AND')
            elif barvalue2 == 'IOS':
                img_figure = cls.get_bar_one(table_data, 1, title=tbvalue + ': IOS')
            elif barvalue2 == 'H5':
                img_figure = cls.get_bar_one(table_data, 2, title=tbvalue + ': H5')
            elif barvalue2 == 'SER':
                img_figure = cls.get_bar_one(table_data, 3, title=tbvalue + ': SER')
            elif barvalue2 == 'PRO':
                img_figure = cls.get_bar_one(table_data, 4, title=tbvalue + ': PRO')
            else:
                img_figure = None
        elif barvalue1 == "Pie":
            if barvalue2 == 'ALL':
                sum_ = cls.get_table_sum(tbvalue)
                img_figure = cls.get_pie(table_data, title=tbvalue + ': ALL' + ' (Num: %s)' % sum_)
            elif barvalue2 == 'AND':
                img_figure = cls.get_pie_one(table_data, 0, title=tbvalue + ': AND')
            elif barvalue2 == 'IOS':
                img_figure = cls.get_pie_one(table_data, 1, title=tbvalue + ': IOS')
            elif barvalue2 == 'H5':
                img_figure = cls.get_pie_one(table_data, 2, title=tbvalue + ': H5')
            elif barvalue2 == 'SER':
                img_figure = cls.get_pie_one(table_data, 3, title=tbvalue + ': SER')
            elif barvalue2 == 'PRO':
                img_figure = cls.get_pie_one(table_data, 4, title=tbvalue + ': PRO')
            else:
                img_figure = None
        else:
            img_figure = None

        return img_figure

    @classmethod
    def get_resolved_data(cls):
        submit_num_data = Data.get_data(TableName.table1.value)
        rest1_num_data = Data.get_data(TableName.table2.value)
        rest2_num_data = Data.get_data(TableName.table3.value)

        resolved_num_data = {}
        for key in Name.gradeList.value:
            sub_data = submit_num_data[key]['data']
            rest1_data = rest1_num_data[key]['data']
            rest2_data = rest2_num_data[key]['data']
            tag_ = submit_num_data[key]['tag']
            res_data = [sub_data[i] + rest2_data[i] - rest1_data[i] for i in range(len(sub_data))]
            res_data = {'data': res_data, 'tag': tag_}
            resolved_num_data[key] = res_data
        return resolved_num_data

    @classmethod
    def get_bar(cls, data, title=''):
        return Image.bar(data, title=title)

    @classmethod
    def get_pie(cls, data, title=''):
        return Image.pie(data, title=title)

    @classmethod
    def get_bar_one(cls, data, index, title=''):
        num_data = data
        one_data = []
        for key, value in num_data.items():
            one_data.append(value['data'][index])
        return Image.bar_one(one_data, title=title + ' (Num: %s)' % sum(one_data))

    @classmethod
    def get_pie_one(cls, data, index, title=''):
        num_data = data
        one_data = []
        for key, value in num_data.items():
            one_data.append(value['data'][index])
        return Image.pie_one(one_data, title=title + ' (Num: %s)' % sum(one_data))

    @classmethod
    def get_table_sum(cls, tableName):
        table_data = Data.get_data(tableName)
        table_sum = 0
        for key, value in table_data.items():
            table_sum += sum(value['data'])
        return table_sum
    @classmethod
    def get_analyze_data(cls):
        submit_sum = cls.get_table_sum(TableName.table1.value)
        rest1_sum = cls.get_table_sum(TableName.table2.value)
        rest2_sum = cls.get_table_sum(TableName.table3.value)
        resolved_sum = submit_sum + rest2_sum - rest1_sum

        ana_data = [
            '本周提交BUG总计: %s 个' % submit_sum,
            '本周剩余BUG总计: %s 个' % rest1_sum,
            '上周剩余BUG总计: %s 个' % rest2_sum,
            '---',
            '本周解决BUG总计: %s 个' % resolved_sum,
        ]
        return ana_data

if __name__ == '__main__':
    GUI_Func.get_resolved_data()