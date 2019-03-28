# -*- coding: utf-8 -*-
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import Tk, Canvas, TOP, BOTH
from image_add.create_img import CreateImg
class Bar():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Bar, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas()
        self.show()
        self.window.mainloop()

    def create_from(self, figure):
        self.canvas = FigureCanvasTkAgg(figure, self.window)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(column=0, row=0, sticky='W', padx=4, pady=4)


        # # 把绘制的图形显示到tkinter窗口上
        # self.canvas = FigureCanvasTkAgg(figure, self.root)
        # self.canvas.draw()  # 以前的版本使用show()方法，matplotlib 2.2之后不再推荐show（）用draw代替，但是用show不会报错，会显示警告
        # self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # # 把matplotlib绘制图形的导航工具栏显示到tkinter窗口上
        # toolbar = NavigationToolbar2Tk(self.canvas,
        #                                self.root)  # matplotlib 2.2版本之后推荐使用NavigationToolbar2Tk，若使用NavigationToolbar2TkAgg会警告
        # toolbar.update()
        # self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
    def show(self):
        figure = CreateImg().bar()
        self.create_from(figure)

if __name__ == '__main__':
    Bar = Bar()

