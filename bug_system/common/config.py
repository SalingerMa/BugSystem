# -*- coding: utf-8 -*-
from enum import Enum

class Name(Enum):
    grade1 = "Bloker"
    grade2 = 'Critical'
    grade3 = 'Major'
    grade4 = 'Minor'
    gradeList = ['Bloker', 'Critical', 'Major', 'Minor']

class Color(Enum):
    color1 = 'blue'
    color2 = 'red'
    color3 = 'yellow'
    color4 = 'green'
    colorList = ['blue', 'red', 'yellow', 'green']

class TableName(Enum):
    table1 = 'submit_bug_of_this_week'
    table2 = 'rest_bug_of_this_week'
    table3 = 'rest_bug_of_last_week'
    nullTable = 'null_table'

class RGB(Enum):
    color1 = '#E0EEEE'
    color2 = '#EE9A00'

class TableHead(Enum):
    column = ['BUG', 'AND', 'IOS', 'H5', 'SER', 'PRO', 'ALL']
    row = ['Bloker', 'Critical', 'Major', 'Minor', 'ALL']

class ImageName(Enum):
    tablelist = [
        'submit_bug_of_this_week',
        'rest_bug_of_this_week',
        'rest_bug_of_last_week',
        'resolved_bug_of_this_week'
    ]
    imglist = [
        'Bar-ALL',
        'Bar-AND',
        'Bar-IOS',
        'Bar-H5',
        'Bar-SER',
        'Bar-PRO',
        'Pie-ALL',
        'Pie-AND',
        'Pie-IOS',
        'Pie-H5',
        'Pie-SER',
        'Pie-PRO'
    ]
    title1 = '本周提交BUG总计'
    title2 = '本周提交BUG总计'
    title3 = '本周提交BUG总计'
    title4 = '本周提交BUG总计'
    title5 = '本周提交BUG总计'



    img_key1 = 'Bar-Table'
    img_key2 = 'Pie-Table'

if __name__ == '__main__':
    print(TableName['sub_table'].value)

