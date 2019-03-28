# -*- coding: utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl

from common.config import Name
class CreateImg:
    def __init__(self):
        pass

    def autolabel(self, rects):
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2 - 0.08, 1.01 * height, '%s' % int(height))

    def bar(self):
        # 创建绘图对象f
        f = plt.figure(figsize=(6.4, 4.8), dpi=100, facecolor="pink", edgecolor='green')
        num_data = {'Bloker': {'data': [1,2,8,4,1], 'tag': 'blue'},
                    'Critical': {'data': [1,0,2,4,5], 'tag': 'red'},
                    'Major': {'data': [1,5,2,0,0], 'tag': 'yellow'},
                    'Minor': {'data': [1,3,2,4,9], 'tag': 'green'}}
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
                self.autolabel(
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
                self.autolabel(
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
                self.autolabel(
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
                self.autolabel(
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

        plt.title('Hello World!')
        return f
