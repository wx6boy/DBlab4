import psycopg2
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
import sys
from psycopg2.extras import RealDictCursor
from datetime import datetime
from sql_functions import create_new_database, all_functions
from designsQt import (first_menu, main_menu, alert_clear)
from connections import main_conn, user_conn
import json


class  FirstMenu(QMainWindow, first_menu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.createButton.clicked.connect(self.creationDB)
        self.openButton.clicked.connect(self.openingDB)
        self.show()

    @pyqtSlot()
    def creationDB(self):
        try:
            user_conn()
            self.errorLabel.setText("DB already exist(you can delete it through opening)")
        except:
            connection = main_conn()
            connection.autocommit = True
            cursor = connection.cursor()
            try:
                cursor.execute(create_new_database)
                cursor.execute("select create_database();")
                cursor.close()
                connection.close()
                connection = user_conn()
                connection.autocommit = True
                cursor = connection.cursor()
                try:
                    cursor.execute(all_functions)
                    cursor.close()
                    self.hide()
                    self.mainMenu = MainMenu(connection=connection)
                    self.mainMenu.show()

                except psycopg2.OperationalError as e:
                    self.errorLabel.setText(f"The error '{e}' was occurred")
                    cursor.close()
                    connection.close()

            except psycopg2.OperationalError as e:
                self.errorLabel.setText(f"The error '{e}' was occurred")
                cursor.close()
                connection.close()

    @pyqtSlot()
    def openingDB(self):
        try:
            connection = user_conn()
            self.hide()
            self.mainMenu = MainMenu(connection=connection)
            self.mainMenu.show()
        except:
            self.errorLabel.setText("DB wasn't created(create it firstly)")



class MainMenu(QMainWindow, main_menu.Ui_MainWindow):
    def __init__(self,connection):
        super().__init__()
        self.setupUi(self)
        self.conn = connection
        self.singerButton.clicked.connect(self.Singers)
        self.songButton.clicked.connect(self.Songs)
        self.deleteButton.clicked.connect(self.DeleteDB)
        self.truncateButton.clicked.connect(self.Truncate)
        self.show()

    @pyqtSlot()
    def Singers(self):
        import singers
        self.hide()
        self.singersMenu = singers.SingersMenu(connection=self.conn)
        self.singersMenu.show()

    @pyqtSlot()
    def Songs(self):
        import songs
        self.hide()
        self.songsMenu = songs.SongsMenu(connection=self.conn)
        self.songsMenu.show()

    @pyqtSlot()
    def DeleteDB(self):
        self.conn.close()
        self.conn = main_conn()
        self.conn.autocommit = True
        cursor = self.conn.cursor()
        try:
            cursor.execute("select drop_database();")
            cursor.close()
            self.conn.close()
            self.hide()
            self.firstMenu = FirstMenu()
            self.firstMenu.show()
        except psycopg2.OperationalError as e:
            self.errorLabel.setText(f"The error '{e}' was occurred")


    @pyqtSlot()
    def Truncate(self):
        self.hide()
        self.conn.autocommit = True
        cursor = self.conn.cursor()
        cursor.execute("select truncate_singers();")
        cursor.close()
        self.alert = clearAllAlert(connection=self.conn)
        self.alert.show()


class clearAllAlert(QMainWindow, alert_clear.Ui_MainWindow):
    def __init__(self,connection):
        super().__init__()
        self.setupUi(self)
        self.conn = connection
        self.pushButton.clicked.connect(self.Back)
        self.show()

    @pyqtSlot()
    def Back(self):
        self.hide()
        self.mainMenu = MainMenu(connection=self.conn)
        self.mainMenu.show()

def main():
    conn = main_conn()
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity "
                   "WHERE pg_stat_activity.datname = 'lab4' AND pid <> pg_backend_pid();")
    cursor.close()
    conn.close()
    app = QApplication(sys.argv)
    window = FirstMenu()
    app.exec_()
if __name__ == '__main__':
    main()


