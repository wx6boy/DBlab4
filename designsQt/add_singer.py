# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_singer.ui'
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
        self.nameLine = QtWidgets.QLineEdit(self.centralwidget)
        self.nameLine.setGeometry(QtCore.QRect(120, 100, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nameLine.setFont(font)
        self.nameLine.setObjectName("nameLine")
        self.ageLine = QtWidgets.QLineEdit(self.centralwidget)
        self.ageLine.setGeometry(QtCore.QRect(120, 210, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ageLine.setFont(font)
        self.ageLine.setObjectName("ageLine")
        self.cityLine = QtWidgets.QLineEdit(self.centralwidget)
        self.cityLine.setGeometry(QtCore.QRect(120, 310, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cityLine.setFont(font)
        self.cityLine.setObjectName("cityLine")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 50, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 160, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 260, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(30, 480, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(660, 480, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(120, 370, 511, 81))
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
        self.label.setText(_translate("MainWindow", "name(character varying)"))
        self.label_2.setText(_translate("MainWindow", "age(integer)"))
        self.label_3.setText(_translate("MainWindow", "city(character varying)"))
        self.backButton.setText(_translate("MainWindow", "BACK"))
        self.addButton.setText(_translate("MainWindow", "ADD"))
