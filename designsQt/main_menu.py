# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
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
        self.singerButton = QtWidgets.QPushButton(self.centralwidget)
        self.singerButton.setGeometry(QtCore.QRect(310, 180, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.singerButton.setFont(font)
        self.singerButton.setObjectName("singerButton")
        self.songButton = QtWidgets.QPushButton(self.centralwidget)
        self.songButton.setGeometry(QtCore.QRect(310, 250, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.songButton.setFont(font)
        self.songButton.setObjectName("songButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(620, 10, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName("deleteButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 90, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(320, 400, 361, 111))
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
        self.truncateButton = QtWidgets.QPushButton(self.centralwidget)
        self.truncateButton.setGeometry(QtCore.QRect(620, 490, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.truncateButton.setFont(font)
        self.truncateButton.setObjectName("truncateButton")
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
        self.singerButton.setText(_translate("MainWindow", "Singers table"))
        self.songButton.setText(_translate("MainWindow", "Songs table"))
        self.deleteButton.setText(_translate("MainWindow", "Delete DB"))
        self.label.setText(_translate("MainWindow", "Choose table to work with"))
        self.truncateButton.setText(_translate("MainWindow", "Truncate tables"))
