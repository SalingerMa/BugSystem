# -*- coding: utf-8 -*-
from enum import Enum

class Name(Enum):
    grade1 = "Bloker"
    grade2 = 'Critical'
    grade3 = 'Major'
    grade4 = 'Minor'

class Color(Enum):
    color1 = 'blue'
    color2 = 'red'
    color3 = 'yellow'
    color4 = 'green'

class TableName(Enum):
    table1 = 'submit_bug_of_this_week'
    table2 = 'rest_bug_of_this_week'
    table3 = 'rest_bug_of_last_week'

class RGB(Enum):
    color1 = '#E0EEEE'
    color2 = '#EE9A00'

class TableHead(Enum):
    column = ['BUG', 'AND', 'IOS', 'H5', 'SER', 'PRO', 'ALL']
    row = ['Bloker', 'Critical', 'Major', 'Minor', 'ALL']



if __name__ == '__main__':
    print(TableName['sub_table'].value)

