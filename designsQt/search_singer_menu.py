# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_singer_menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.allButton = QtWidgets.QPushButton(self.centralwidget)
        self.allButton.setGeometry(QtCore.QRect(300, 320, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.allButton.setFont(font)
        self.allButton.setObjectName("allButton")
        self.nameButton = QtWidgets.QPushButton(self.centralwidget)
        self.nameButton.setGeometry(QtCore.QRect(300, 110, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nameButton.setFont(font)
        self.nameButton.setObjectName("nameButton")
        self.cityButton = QtWidgets.QPushButton(self.centralwidget)
        self.cityButton.setGeometry(QtCore.QRect(300, 250, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cityButton.setFont(font)
        self.cityButton.setObjectName("cityButton")
        self.ageButton = QtWidgets.QPushButton(self.centralwidget)
        self.ageButton.setGeometry(QtCore.QRect(300, 180, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ageButton.setFont(font)
        self.ageButton.setObjectName("ageButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 477, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(350, 450, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.errorLabel.setFont(font)
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
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
        self.allButton.setText(_translate("MainWindow", "Show full table"))
        self.nameButton.setText(_translate("MainWindow", "Search by name"))
        self.cityButton.setText(_translate("MainWindow", "Search by city"))
        self.ageButton.setText(_translate("MainWindow", "Search by age"))
        self.pushButton.setText(_translate("MainWindow", "Back"))
