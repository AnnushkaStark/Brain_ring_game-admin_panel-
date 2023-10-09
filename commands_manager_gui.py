from typing import Self, TextIO
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget
import sys
from PyQt6 import *
import sqlite3 as sql
from commands import *

class Commands(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.database = 'app/assets/database/brainring.db'
        self.querry_add_single = '''INSERT INTO single_game (team_name, winners) VALUES (?,?)''' # Этот запрос регистрирует команду в одиноной игре
        self.querry_add_tournier = '''INSERT INTO tournier (team_name, winners) VALUES (?,?)''' # Этот запрос регистрирует команду в турнире
        self.querry_delet_single ='''DELET FROM single_game WHERE team_name LIKE ?''' # Этот запрос удаляет команду из рейтинга одиночной игры
        self.querry_delet_tourinier ='''DELET FROM tournier WHERE team_name LIKE ?''' # Этот запрос удаляет команду из рейтинга турнира
        self.querry_change_single = ''' UPDATE single_game SET team_name = ? WHERE team_name LIKE ?'''#Этот запрос измняет название команды в рейтинге одиночной игры
        self.querry_change_tournier = ''' UPDATE tournier SET team_name = ? WHERE team_name LIKE ?'''#Этот запрос измняет название команды в рейтинге турнира
        self.raiting = 0 # Количество  побед по умолчанию 0 при добавлении новой команды
        self.pushButton_add_single.clicked.connect(self.add_single)
        self.pushButton_change_single.clicked.connect(self.change_single)
        self.pushButton_delet_single.clicked.connect(self.delet_single)
        self.pushButton_add_tournier.clicked.connect(self.add_tournier)
        self.pushButton_change_tournier.clicked.connect(self.change_tournier)
        self.pushButton_delet_tournier.clicked.connect(self.delet_tournier)

    def add_single(self):
        ''''Эта функуция добавляет новую команду в  одиночную игру'''
        try:
            with sql.connect(self.database) as conn:
                self.team_name = self.lineEdit_team_single.text()
                self.raiting = 0
                if self.team_name.strip():
                    conn.cursor().execute(self.querry_add_single,(self.team_name,self.raiting))
                    result = QMessageBox()
                    result.setText(f'Команда {self.team_name} добавлена')
                    result.exec()
        except sql.IntegrityError:
            result = QMessageBox()
            result.setText('Error')
            result.exec()
        except sql.OperationalError:
            result = QMessageBox()
            result.setText('Error')
            result.exec()
        except TypeError:
            result = QMessageBox()
            result.setText('Error')
            result.exec()
        except ValueError:
            result = QMessageBox()
            result.setText('Error')
            result.exec()



    def change_single(self):
        pass

    def delet_single(self):
        pass

    def add_tournier(self):
        '''Эта функция добавляет команду в турнир'''
        try:
            with sql.connect(self.database) as conn:
                self.team_name = self.lineEdit_team_tournier.text()
                self.raiting = 0
                if self.team_name.strip():
                    conn.cursor().execute(self.querry_add_tournier,(self.team_name,self.raiting))
                    result = QMessageBox()
                    result.setText(f'Команда {self.team_name} добавлена')
                    result.exec()
        except sql.IntegrityError:
            result = QMessageBox()
            result.setText('Error')
            result.exec()
        except sql.OperationalError:
            result = QMessageBox()
            result.setText('Error')
            result.exec()
        except TypeError:
            result = QMessageBox()
            result.setText('Error')
            result.exec()
        except ValueError:
            result = QMessageBox()
            result.setText('Error')
            result.exec()



    def change_tournier(self):
        pass

    def delet_tournier(self):
        pass
