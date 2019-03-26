# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bug1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1158, 837)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.submit_table = QtWidgets.QTableWidget(self.centralwidget)
        self.submit_table.setGeometry(QtCore.QRect(80, 21, 971, 661))
        self.submit_table.setObjectName("submit_table")
        self.submit_table.setColumnCount(2)
        self.submit_table.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.submit_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.submit_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.submit_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.submit_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.submit_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.submit_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
        self.submit_table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.submit_table.setItem(1, 1, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1158, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.submit_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "r1"))
        item = self.submit_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "r2"))
        item = self.submit_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "A"))
        item = self.submit_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "B"))
        __sortingEnabled = self.submit_table.isSortingEnabled()
        self.submit_table.setSortingEnabled(False)
        item = self.submit_table.item(0, 0)
        item.setText(_translate("MainWindow", "fjfd"))
        item = self.submit_table.item(0, 1)
        item.setText(_translate("MainWindow", "dfdsa"))
        item = self.submit_table.item(1, 0)
        item.setText(_translate("MainWindow", "dfag"))
        item = self.submit_table.item(1, 1)
        item.setText(_translate("MainWindow", "dfasdf"))
        self.submit_table.setSortingEnabled(__sortingEnabled)

