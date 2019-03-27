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
        MainWindow.resize(1158, 841)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.submit_table = QtWidgets.QTableWidget(self.centralwidget)
        self.submit_table.setGeometry(QtCore.QRect(20, 40, 611, 221))
        self.submit_table.setObjectName("submit_table")
        self.submit_table.setColumnCount(0)
        self.submit_table.setRowCount(0)
        self.submit_table.horizontalHeader().setDefaultSectionSize(70)
        self.rest_table = QtWidgets.QTableWidget(self.centralwidget)
        self.rest_table.setGeometry(QtCore.QRect(20, 300, 611, 221))
        self.rest_table.setObjectName("rest_table")
        self.rest_table.setColumnCount(0)
        self.rest_table.setRowCount(0)
        self.rest_table.horizontalHeader().setDefaultSectionSize(70)
        self.old_rest_table = QtWidgets.QTableWidget(self.centralwidget)
        self.old_rest_table.setGeometry(QtCore.QRect(20, 570, 611, 221))
        self.old_rest_table.setObjectName("old_rest_table")
        self.old_rest_table.setColumnCount(0)
        self.old_rest_table.setRowCount(0)
        self.old_rest_table.horizontalHeader().setDefaultSectionSize(70)
        self.refresh_button = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_button.setGeometry(QtCore.QRect(670, 50, 71, 28))
        self.refresh_button.setObjectName("refresh_button")
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
        self.refresh_button.setText(_translate("MainWindow", "refresh"))

