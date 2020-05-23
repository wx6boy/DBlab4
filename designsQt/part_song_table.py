# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'part_singer_table.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, my_list):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        gridLayout = QtWidgets.QGridLayout()
        self.centralwidget.setLayout(gridLayout)

        table = QtWidgets.QTableWidget(self)
        table.setColumnCount(4)
        table.setRowCount(len(my_list))
        headers = ['auth_id', 'song_id','song_name', 'modification_time']
        table.setHorizontalHeaderLabels(headers)

        for row in range(len(my_list)):
            for col in range(4):
                table.setItem(row, col, QtWidgets.QTableWidgetItem(str(my_list[row][headers[col]])))
        table.resizeColumnsToContents()

        gridLayout.addWidget(table, 0, 0)
        self.backB = QtWidgets.QPushButton(self.centralwidget)
        self.backB.setGeometry(QtCore.QRect(20, 610, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.backB.setFont(font)
        self.backB.setObjectName("backB")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.backB.setText(_translate("MainWindow", "Back"))
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
