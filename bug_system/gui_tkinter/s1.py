# import tkinter
# from tkinter import ttk  # 导入内部包
#
# win = tkinter.Tk()
# tree = ttk.Treeview(win)  # 表格
# tree["columns"] = ("姓名", "年龄", "身高")
# tree.column("姓名", width=100)  # 表示列,不显示
# tree.column("年龄", width=100)
# tree.column("身高", width=100)
#
# tree.heading("姓名", text="姓名-name")  # 显示表头
# tree.heading("年龄", text="年龄-age")
# tree.heading("身高", text="身高-tall")
#
# tree.insert("", 0, text="line1", values=("1", "2", "3"))  # 插入数据，
# tree.insert("", 1, text="line1", values=("1", "2", "3"))
# tree.insert("", 2, text="line1", values=("1", "2", "3"))
# tree.insert("", 3, text="line1", values=("1", "2", "3"))
#
# tree.pack()
# win.mainloop()

from tkinter import ttk
from tkinter import *

root = Tk()  # 初始框的声明
columns = ("姓名", "IP地址")
treeview = ttk.Treeview(root, height=18, show="headings", columns=columns)  # 表格

treeview.column("姓名", width=100, anchor='center')  # 表示列,不显示
treeview.column("IP地址", width=300, anchor='center')

treeview.heading("姓名", text="姓名")  # 显示表头
treeview.heading("IP地址", text="IP地址")

treeview.pack(side=LEFT, fill=BOTH)
treeview.tag_configure('a', background='yellow')

name = ['电脑1', '服务器', '笔记本']
ipcode = ['10.13.71.223', '10.25.61.186', '10.25.11.163']
for i in range(min(len(name), len(ipcode))):  # 写入数据
    treeview.insert('', i, values=(name[i], ipcode[i]))
print(treeview.get_children())

print(treeview.item('I003'))
root.mainloop()  # 进入消息循环
