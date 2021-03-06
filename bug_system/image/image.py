# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from common.mysqler import SQL
from common.config import Name, Color
import numpy as np
img_width = 5.3
img_hight = 4.7
img_dpi = 100

class Data:
    @classmethod
    def get_data(cls, table):
        data = SQL.select(table)
        num_data = {}
        for item in data:
            num_list_name = item[0]
            tag = Data.get_tag(num_list_name)
            num_list_data = {'data': list(item[1:]), 'tag': tag}
            num_data[num_list_name] = num_list_data
        return num_data

    @classmethod
    def get_tag(cls, value):
        if value == Name.grade1.value:
            tag = Color.color1.value
        elif value == Name.grade2.value:
            tag = Color.color2.value
        elif value == Name.grade3.value:
            tag = Color.color3.value
        elif value == Name.grade4.value:
            tag = Color.color4.value
        return tag

    @classmethod
    def get_res_data(cls):
        pass

class Image:
    # 定义函数来显示柱状上的数值
    @classmethod
    def autolabel(cls, rects):
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2 - 0.08, 1.0 * height, '%s' % int(height))
    @classmethod
    def bar(cls, num_data, title='bar chart'):
        """

        :param table: 数据表名
        :param title: 柱形图标题
        :return: 返回一张图片
        """
        f = plt.figure(figsize=(img_width, img_hight), dpi=img_dpi, facecolor="pink", edgecolor='green')
        # num_data = Data.get_data(table)
        # print(num_data)
        name_list = ['AND', 'IOS', 'H5', 'SER', 'PRO']
        total_width, n = 0.6, 4
        width = total_width / n
        x = list(range(len(name_list)))
        x1 = x
        x2 = [ i + width for i in x1]
        x3 = [ i + width for i in x2]
        x4 = [ i + width for i in x3]

        for key, value in num_data.items():
            if key == Name.grade1.value:
                Image.autolabel(
                    plt.bar(
                        x1,
                        value['data'],
                        label=key,
                        color=value['tag'],
                        width=width,
                        align='edge',
                        alpha=0.5,
                    )
                )
            elif key == Name.grade2.value:
                Image.autolabel(
                    plt.bar(
                        x2,
                        value['data'],
                        label=key,
                        color=value['tag'],
                        width=width,
                        align='edge'
                    )
                )
            elif key == Name.grade3.value:
                Image.autolabel(
                    plt.bar(
                        x3,
                        value['data'],
                        label=key,
                        color=value['tag'],
                        width=width,
                        align='edge',
                        tick_label=name_list
                    )
                )
            elif key == Name.grade4.value:
                Image.autolabel(
                    plt.bar(
                        x4,
                        value['data'],
                        label=key,
                        color=value['tag'],
                        width=width,
                        align='edge'
                    )
                )

        plt.legend()
        plt.title(title)
        return f

    @classmethod
    def pie(cls, pie_bug_data, title='pie chart'):
        q = plt.figure(figsize=(img_width, img_hight), dpi=img_dpi, facecolor="pink", edgecolor='green')

        pie_label = []
        pie_num = []
        pie_color = []
        pie_indic = []
        for key,value in pie_bug_data.items():
            pie_label.append(key)
            pie_num.append(sum(value['data']))
            pie_color.append(value['tag'])

        sum_pie_num = sum(pie_num)
        pie_num = [num / sum_pie_num for num in pie_num]
        # print(pie_num)
        # 我们将数据最大的突出显示
        for num in pie_num:
            if num == max(pie_num):
                pie_indic.append(0.1)
            else:
                pie_indic.append(0)

        plt.pie(
            pie_num,
            labels=pie_label,
            colors=pie_color,
            startangle=90,
            shadow=True,
            explode=tuple(pie_indic),  # tuple方法用于将列表转化为元组
            autopct='%1.1f%%'  # 是数字1，不是l
        )
        plt.title(title)
        return q

    @classmethod
    def bar_one(cls, one_data, title=''):
        f1 = plt.figure(figsize=(img_width, img_hight), dpi=img_dpi, facecolor="pink", edgecolor='green')

        name_list = Name.gradeList.value
        width = 0.6
        scan = np.arange(4)
        Image.autolabel(
            plt.bar(
                scan,
                one_data,
                color=Color.colorList.value,
                width=width,
                align='center',
                alpha=0.5,
            )
        )
        plt.xticks(scan, name_list)
        plt.title(title)
        return f1

    @classmethod
    def pie_one(cls, one_data, title=''):
        q1 = plt.figure(figsize=(img_width, img_hight), dpi=img_dpi, facecolor="pink", edgecolor='green')
        # pie_bug_data = Data.get_data(table)
        # print(pie_bug_data)
        pie_label = Name.gradeList.value
        pie_num = one_data
        pie_color = Color.colorList.value
        pie_indic = []

        sum_pie_num = sum(pie_num)
        pie_num = [num / sum_pie_num for num in pie_num]
        # print(pie_num)
        # 我们将数据最大的突出显示
        for num in pie_num:
            if num == max(pie_num):
                pie_indic.append(0.1)
            else:
                pie_indic.append(0)

        plt.pie(
            pie_num,
            labels=pie_label,
            colors=pie_color,
            startangle=90,
            shadow=True,
            explode=tuple(pie_indic),  # tuple方法用于将列表转化为元组
            autopct='%1.1f%%'  # 是数字1，不是l
        )
        plt.title(title)
        return q1

    @classmethod
    def bar_extend(cls):
        pass
    @classmethod
    def pie_extend(cls):
        pass

if __name__ == '__main__':
    pass
    # f = Image.pie_one('submit_bug_of_this_week', index=2, title='Submit BUG of This Week')
    # f.show()
    # Image.pie('submit_bug_of_this_week', title='Submit BUG of This Week', save_name='pie_1.png')