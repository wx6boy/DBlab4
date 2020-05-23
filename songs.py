import psycopg2
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
from psycopg2.extras import RealDictCursor
from datetime import datetime
from designsQt import (add_song, songs_menu, change_song, delete_song, search_song_menu, part_song_table,
                       particularly_search_singer, alert_clear)
import json
from connections import DateEncoder


class SongsMenu(QMainWindow, songs_menu.Ui_MainWindow):
    def __init__(self,connection):
        super().__init__()
        self.setupUi(self)
        self.conn = connection
        self.addButton.clicked.connect(self.Addition)
        self.changeButton.clicked.connect(self.Changing)
        self.deleteButton.clicked.connect(self.Deletion)
        self.showButton.clicked.connect(self.Show)
        self.backButton.clicked.connect(self.Back)
        self.truncateButton.clicked.connect(self.Truncate)
        self.show()


    @pyqtSlot()
    def Deletion(self):
        self.hide()
        self.deleteSong = DeleteSong(connection=self.conn)
        self.deleteSong.show()


    @pyqtSlot()
    def Truncate(self):
        self.hide()
        self.conn.autocommit = True
        cursor = self.conn.cursor()
        cursor.execute("select truncate_songs();")
        cursor.close()
        self.alert = clearAlert(connection=self.conn)
        self.alert.show()

    @pyqtSlot()
    def Changing(self):
        self.hide()
        self.changeSong = ChangeSong(connection=self.conn)
        self.changeSong.show()

    @pyqtSlot()
    def Addition(self):
        self.hide()
        self.addSong = AddSong(connection=self.conn)
        self.addSong.show()
        
    @pyqtSlot()
    def Show(self):
        self.hide()
        self.searchMenu = SearchSongMenu(connection=self.conn)
        self.searchMenu.show()

    @pyqtSlot()
    def Back(self):
        from my_gui import MainMenu
        self.hide()
        self.mainMenu = MainMenu(connection=self.conn)
        self.mainMenu.show()
        
        
class AddSong(QMainWindow, add_song.Ui_MainWindow):
    def __init__(self,connection):
        super().__init__()
        self.setupUi(self)
        self.conn = connection
        self.addButton.clicked.connect(self.Addition)
        self.backButton.clicked.connect(self.Back)
        self.show()


    @pyqtSlot()
    def Addition(self):
        id = self.idLine.text()
        name = self.nameLine.text()
        if name and id:
            self.conn.autocommit = True
            cursor = self.conn.cursor()
            try:
                cursor.execute(f"select insert_song('{id}','{name}');")
                cursor.close()
                self.errorLabel.setText("Data were added successfully")
                self.idLine.clear()
                self.nameLine.clear()
            except psycopg2.Error as e:
                self.errorLabel.setText(f"The error '{e}' was occurred")
        else:
            self.errorLabel.setText("You need to fill up all the gaps")

    @pyqtSlot()
    def Back(self):
        self.hide()
        self.songMenu = SongsMenu(connection=self.conn)
        self.songMenu.show()
        
        
class ChangeSong(QMainWindow, change_song.Ui_MainWindow):
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
            cursor.execute(f"select check_song('{id}');")
            result = cursor.fetchall()
            if result != [(None,)]:
                name = self.nameLine.text()
                if name:
                    try:
                        cursor.execute(f"select update_song_name('{id}','{name}');")
                        self.errorLabel.setText("Info was updated successfully")
                        self.idLine.clear()
                        self.nameLine.clear()
                    except psycopg2.Error as e:
                        self.errorLabel.setText(f"The error '{e}' was occurred")
                else:
                    self.errorLabel.setText("Fill up info for changing")
            else:
                self.errorLabel.setText(f"Data with id = {id} doesnt exists")
                self.idLine.clear()
        else:
            self.errorLabel.setText("ID line is empty")

    @pyqtSlot()
    def Back(self): 
        self.hide()
        self.songsMenu = SongsMenu(connection=self.conn)
        self.songsMenu.show()
        
        
class DeleteSong(QMainWindow, delete_song.Ui_MainWindow):
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
                cursor.execute(f"select check_song('{id}');")
                result = cursor.fetchall()
                if result != [(None,)]:
                    cursor.execute(f"select delete_particular_song('{id}');")
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
        self.songsMenu = SongsMenu(connection=self.conn)
        self.songsMenu.show()
        

class clearAlert(QMainWindow, alert_clear.Ui_MainWindow):
    def __init__(self,connection):
        super().__init__()
        self.setupUi(self)
        self.conn = connection
        self.pushButton.clicked.connect(self.Back)
        self.show()

    @pyqtSlot()
    def Back(self):
        self.hide()
        self.songsMenu = SongsMenu(connection=self.conn)
        self.songsMenu.show()


class SearchSongMenu(QMainWindow, search_song_menu.Ui_MainWindow):
    def __init__(self,connection):  
        super().__init__()
        self.setupUi(self)
        self.conn = connection
        self.nameButton.clicked.connect(self.ByName)
        self.allButton.clicked.connect(self.FullTable)
        self.pushButton.clicked.connect(self.Back)
        self.show()

    @pyqtSlot()
    def ByName(self):
        self.hide()
        self.partSearch = PartSearchSong(connection=self.conn, part='song_name')
        self.partSearch.show()

    @pyqtSlot()
    def FullTable(self):
        self.conn.autocommit = True
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("select get_all_songs();")
        results = json.loads(json.dumps(cursor.fetchall(),cls=DateEncoder))
        if results[0]['get_all_songs']:
            self.hide()
            self.partSearchTb = PartSongTable(connection=self.conn, mylist=results[0]['get_all_songs'])
            self.partSearchTb.show()
        else:
            self.errorLabel.setText('Table is empty')

    @pyqtSlot()
    def Back(self):
        self.hide()
        self.songsMenu = SongsMenu(connection=self.conn)
        self.songsMenu.show()


class PartSearchSong(QMainWindow, particularly_search_singer.Ui_MainWindow):
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
                cursor.execute(f"select get_songs_by_name('{self.lineEdit.text()}');")
                results = json.loads(json.dumps(cursor.fetchall(),cls=DateEncoder))
                if results[0][f'get_songs_by_name']:
                    self.hide()
                    self.partSearchTb = PartSongTable(connection=self.conn,
                                                        mylist=results[0][f'get_songs_by_name'])
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
        self.searchSong = SearchSongMenu(connection=self.conn)
        self.searchSong.show()


class PartSongTable(QMainWindow, part_song_table.Ui_MainWindow):
    def __init__(self, connection, mylist):
        super().__init__()
        self.setupUi(self, my_list=mylist)
        self.conn = connection
        self.backB.clicked.connect(self.Back)
        self.show()

    @pyqtSlot()
    def Back(self):
        self.hide()
        self.searchSong = SearchSongMenu(connection=self.conn)
        self.searchSong.show()
        
        