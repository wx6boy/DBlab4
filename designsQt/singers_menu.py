# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'singers_menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 30, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(300, 110, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.changeButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeButton.setGeometry(QtCore.QRect(300, 180, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.changeButton.setFont(font)
        self.changeButton.setObjectName("changeButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(300, 250, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName("deleteButton")
        self.showButton = QtWidgets.QPushButton(self.centralwidget)
        self.showButton.setGeometry(QtCore.QRect(300, 320, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.showButton.setFont(font)
        self.showButton.setObjectName("showButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(40, 477, 101, 41))
        self.backButton.setObjectName("backButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.label.setText(_translate("MainWindow", "Singers table"))
        self.addButton.setText(_translate("MainWindow", "Add data"))
        self.changeButton.setText(_translate("MainWindow", "Change info"))
        self.deleteButton.setText(_translate("MainWindow", "Delete data"))
        self.showButton.setText(_translate("MainWindow", "Show data"))
        self.backButton.setText(_translate("MainWindow", "Back"))
