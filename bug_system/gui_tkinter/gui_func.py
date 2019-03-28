# -*- coding: utf-8 -*-
from common.function import Common
from common.config import TableHead
import os
from PIL import Image

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

    @classmethod
    def ensure_path(cls, base_path):
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        else:
            return None
    @classmethod
    def clean_file(cls, path):
        for i in os.listdir(path):
            path_file = os.path.join(path, i)
            if os.path.isfile(path_file):
                os.remove(path_file)

    @classmethod
    def IsValidImage(cls, img_path):
        """
        判断文件是否为有效（完整）的图片
        :param img_path:图片路径
        :return:True：有效 False：无效
        """
        bValid = True
        try:
            Image.open(img_path).verify()
        except:
            bValid = False
        return bValid

    @classmethod
    def transimg(cls, img_path):
        """
        转换图片格式
        :param img_path:图片路径
        :return: True：成功 False：失败
        """
        if cls.IsValidImage(img_path):
            try:
                str = img_path.rsplit(".", 1)
                output_img_path = str[0] + ".gif"
                im = Image.open(img_path)
                im.save(output_img_path)
                return output_img_path
            except:
                return False
        else:
            return False

if __name__ == '__main__':
    a = GUI_Func.transimg(r'C:\GitHub\BugSystem\bug_system\gui_tkinter\images\submit_bug_of_this_week.jpg')
    print(a)