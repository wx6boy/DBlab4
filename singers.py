import psycopg2
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
from psycopg2.extras import RealDictCursor
from datetime import datetime
from designsQt import (singers_menu, add_singer,delete_singer, change_singer, search_singer_menu,
                       particularly_search_singer,part_singer_table)
import json

class SingersMenu(QMainWindow, singers_menu.Ui_MainWindow):
    def __init__(self, connection):
        super().__init__()
        self.setupUi(self)
        self.conn = connection
        self.addButton.clicked.connect(self.Addition)
        self.changeButton.clicked.connect(self.Changing)
        self.deleteButton.clicked.connect(self.Deletion)
        self.showButton.clicked.connect(self.Show)
        self.backButton.clicked.connect(self.Back)
        self.show()

    @pyqtSlot()
    def Deletion(self):
        self.hide()
        self.deleteSinger = DeleteSinger(connection=self.conn)
        self.deleteSinger.show()

    @pyqtSlot()
    def Changing(self):
        self.hide()
        self.changeSinger = ChangeSinger(connection=self.conn)
        self.changeSinger.show()

    @pyqtSlot()
    def Addition(self):
        self.hide()
        self.addSinger = AddSinger(connection=self.conn)
        self.addSinger.show()

    @pyqtSlot()
    def Show(self):
        self.hide()
        self.searchSinger = SearchSingerMenu(connection=self.conn)
        self.searchSinger.show()

    @pyqtSlot()
    def Back(self):
        from my_gui import MainMenu
        self.hide()
        self.mainMenu = MainMenu(connection=self.conn)
        self.mainMenu.show()

class DeleteSinger(QMainWindow, delete_singer.Ui_MainWindow):
    def __init__(self,connection):
        super().__init__()
        self.setupUi(self)
        self.conn = connection
        self.deleteButton.clicked.connect(self.Deletion)
        self.backButton.clicked.connect(self.Back)
        self.show()

    @pyqtSlot()
    def Deletion(self):
        id = self.idLine.text()
        if id:
            self.conn.autocommit = True
            cursor = self.conn.cursor()
            try:
                cursor.execute(f"select check_singer('{id}');")
                result = cursor.fetchall()
                if result != [(None,)]:
                    cursor.execute(f"select delete_particular_singer('{id}');")
                    cursor.close()
                    self.errorLabel.setText(f"Data with id = {id} were dropped successfully")
                    self.idLine.clear()
                else:
                    self.errorLabel.setText(f"Data with id = {id} doesnt exists")
                    self.idLine.clear()
            except psycopg2.Error as e:
                self.errorLabel.setText(f"The error '{e}' was occurred")
        else:
            self.errorLabel.setText("You fill up the id line")

    @pyqtSlot()
    def Back(self):
        self.hide()
        self.singerMenu = SingersMenu(connection=self.conn)
        self.singerMenu.show()

class AddSinger(QMainWindow, add_singer.Ui_MainWindow):
    def __init__(self,connection):
        super().__init__()
        self.setupUi(self)
        self.conn = connection
        self.addButton.clicked.connect(self.Addition)
        self.backButton.clicked.connect(self.Back)
        self.show()


    @pyqtSlot()
    def Addition(self):
        name = self.nameLine.text()
        age = self.ageLine.text()
        city = self.cityLine.text()
        if name and age and city:
            self.conn.autocommit = True
            cursor = self.conn.cursor()
            try:
                cursor.execute(f"select insert_singer('{name}','{age}','{city}');")
                cursor.close()
                self.errorLabel.setText("Data were added successfully")
            except psycopg2.Error as e:
                self.errorLabel.setText(f"The error '{e}' was occurred")
        else:
            self.errorLabel.setText("You need to fill up all the gaps")

    @pyqtSlot()
    def Back(self):
        self.hide()
        self.singerMenu = SingersMenu(connection=self.conn)
        self.singerMenu.show()


class ChangeSinger(QMainWindow, change_singer.Ui_MainWindow):
    def __init__(self,connection):
        super().__init__()
        self.setupUi(self)
        self.conn = connection
        self.changeButton.clicked.connect(self.Change)
        self.backButton.clicked.connect(self.Back)
        self.show()

    @pyqtSlot()
    def Change(self):
        id = self.idLine.text()
        if id:
            self.conn.autocommit = True
            cursor = self.conn.cursor()
            cursor.execute(f"select check_singer('{id}');")
            result = cursor.fetchall()
            if result != [(None,)]:
                name = self.nameLine.text()
                age = self.ageLine.text()
                city = self.cityLine.text()
                fl = 0
                fl_m = 0
                if name:
                    fl = 1
                    try:
                        cursor.execute(f"select update_singer_name('{id}','{name}');")
                    except psycopg2.Error as e:
                        fl_m = 1
                        self.errorLabel.setText(f"The error '{e}' was occurred")
                if age and fl_m == 0:
                    fl = 1
                    try:
                        cursor.execute(f"select update_singer_age('{id}','{age}');")
                    except psycopg2.Error as e:
                        fl_m = 1
                        self.errorLabel.setText(f"The error '{e}' was occurred")
                if city and fl_m == 0:
                    fl = 1
                    try:
                        cursor.execute(f"select update_singer_city('{id}','{city}');")
                    except psycopg2.Error as e:
                        fl_m = 1
                        self.errorLabel.setText(f"The error '{e}' was occurred")
                if fl == 1 and fl_m == 0:
                    self.errorLabel.setText("Info was updated successfully")
                    self.idLine.clear()
                    self.nameLine.clear()
                    self.ageLine.clear()
                    self.cityLine.clear()
                elif fl == 0:
                    self.errorLabel.setText("Fill up info for changing")
            else:
                self.errorLabel.setText(f"Data with id = {id} doesnt exists")
                self.idLine.clear()
        else:
            self.errorLabel.setText("ID line is empty")

    @pyqtSlot()
    def Back(self):
        self.hide()
        self.singerMenu = SingersMenu(connection=self.conn)
        self.singerMenu.show()


class SearchSingerMenu(QMainWindow, search_singer_menu.Ui_MainWindow):
    def __init__(self,connection):
        super().__init__()
        self.setupUi(self)
        self.conn = connection
        self.nameButton.clicked.connect(self.ByName)
        self.ageButton.clicked.connect(self.ByAge)
        self.cityButton.clicked.connect(self.ByCity)
        self.allButton.clicked.connect(self.FullTable)
        self.pushButton.clicked.connect(self.Back)
        self.show()

    @pyqtSlot()
    def ByName(self):
        self.hide()
        self.partSearch = PartSearchSinger(connection=self.conn, part='name')
        self.partSearch.show()

    @pyqtSlot()
    def ByAge(self):
        self.hide()
        self.partSearch = PartSearchSinger(connection=self.conn, part='age')
        self.partSearch.show()
    @pyqtSlot()
    def ByCity(self):
        self.hide()
        self.partSearch = PartSearchSinger(connection=self.conn, part='city')
        self.partSearch.show()

    @pyqtSlot()
    def FullTable(self):
        self.conn.autocommit = True
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("select get_all_singers();")
        results = json.loads(json.dumps((cursor.fetchall())))
        if results[0]['get_all_singers']:
            self.hide()
            self.partSearchTb = PartSingerTable(connection=self.conn, mylist=results[0]['get_all_singers'])
            self.partSearchTb.show()
        else:
            self.errorLabel.setText('Table is empty')

    @pyqtSlot()
    def Back(self):
        self.hide()
        self.singerMenu = SingersMenu(connection=self.conn)
        self.singerMenu.show()


class PartSearchSinger(QMainWindow, particularly_search_singer.Ui_MainWindow):
    def __init__(self, connection, part):
        super().__init__()
        self.setupUi(self)
        self.part = part
        self.conn = connection
        self.mainLabel.setText(f"Input {self.part}")
        self.searchButton.clicked.connect(self.Search)
        self.backButton.clicked.connect(self.Back)
        self.show()

    @pyqtSlot()
    def Search(self):
        self.conn.autocommit = True
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        if self.lineEdit.text():
            try:
                cursor.execute(f"select get_singers_by_{self.part}('{self.lineEdit.text()}');")
                results = json.loads(json.dumps((cursor.fetchall())))
                if results[0][f'get_singers_by_{self.part}']:
                    self.hide()
                    self.partSearchTb = PartSingerTable(connection=self.conn,
                                                        mylist=results[0][f'get_singers_by_{self.part}'])
                    self.partSearchTb.show()
                else:
                    self.errorLabel.setText(f'There is no info with {self.part}={self.lineEdit.text()}')
                    self.lineEdit.clear()
            except psycopg2.Error as e:
                self.errorLabel.setText(f"The error '{e}' was occurred")
                self.lineEdit.clear()
        else:
            self.errorLabel.setText('You need to write info to find')
    @pyqtSlot()
    def Back(self):
        self.hide()
        self.searchSinger = SearchSingerMenu(connection=self.conn)
        self.searchSinger.show()


class PartSingerTable(QMainWindow, part_singer_table.Ui_MainWindow):
    def __init__(self, connection, mylist):
        super().__init__()
        self.setupUi(self,my_list=mylist)
        self.conn = connection
        self.backB.clicked.connect(self.Back)
        self.show()
        
    @pyqtSlot()
    def Back(self):
        self.hide()
        self.searchSinger = SearchSingerMenu(connection=self.conn)
        self.searchSinger.show()