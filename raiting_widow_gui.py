from typing import Self, TextIO
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget
import sys
from PyQt6 import *
import sqlite3 as sql
from raiting_window import *




class Raiting(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.database = 'app/assets/database/brainring.db'
        self.querry_single_game = '''SELECT ID, team_name, winners FROM single_game ORDER BY winners''' #этот запрос выводит рейтинг одиночной игры
        self.qurry_tournier = '''SELECT ID, team_name, winners FROM tournier ORDER BY winners''' #этот запрос выводит рейтинг турнира
        self.update_single = '''UPDATE  single_game SET winners = ? WHERE team_name LIKE ?'''# этот запрос увеличивает количесво побед у определенной команды при победе в одиночной игре
        self.update_tournier = '''UPDATE  tournier SET winners = ? WHERE team_name LIKE ?'''# этот запрос увеличивает количесво побед у определенной команды при победе в турнире
        self.querry_found_single = '''SELECT winners FROM single_game WHERE team_name LIKE ?'''#Этот запрос выводит рейтинг командв в одиночной игре чтобы при изменении ретинга увеличить его
        self.querry_found_tournier = '''SELECT winners FROM tournier WHERE team_name LIKE ?'''#Этот запрос выводит рейтинг командв в турнире чтобы при изменении ретинга увеличить его
        self.pushButton_Singe_Game.clicked.connect(self.single_game)
        self.pushButton_Toutnier.clicked.connect(self.tournier)
        self.pushButton_change_single_game.clicked.connect(self.change_raiting_single)
        self.pushButton_change_tourner.clicked.connect(self.change_raiting_tournier)


    def single_game(self):
        '''Эта функция выводит в таблицу рейтинг одиночной игры'''
        try:
            with sql.connect(self.database ) as conn:
                result = conn.cursor().execute(self.querry_single_game).fetchall()
                self.tableWidget.setRowCount(len(result))
                self.tableWidget.setColumnCount(len(result[0]))
                for row in range(len(result)):
                    for column in range(len(result[row])):
                        item = QTableWidgetItem(str(result[row][column]))
                        self.tableWidget.setItem(row,column,item)
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
            


    def tournier(self):
        '''Эта функция выводит в таблицу рейтинг турнира'''
        try:
            with sql.connect(self.database ) as conn:
                result = conn.cursor().execute(self.qurry_tournier).fetchall()
                self.tableWidget.setRowCount(len(result))
                self.tableWidget.setColumnCount(len(result[0]))
                for row in range(len(result)):
                    for column in range(len(result[row])):
                        item = QTableWidgetItem(str(result[row][column]))
                        self.tableWidget.setItem(row,column,item)
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
       
    def change_raiting_single(self):
        '''Эта функция увеличивает рейтинг команды при победе в одиночной игре'''
        try:
            with sql.connect(self.database) as conn:
                self.team_name = self.lineEdit_single_team.text()
                if self.team_name.strip():
                    res = conn.cursor().execute(self.querry_found_single,(self.team_name,))
                    for row in res:
                        new= row[0]
                        new += 1
                        res = conn.cursor().execute(self.update_single,(new,self.team_name))
                        result = QMessageBox()
                        result.setText(f'Рейтинг команды {self.team_name} обновлен')
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


    def change_raiting_tournier(self):
        '''Эта функция увеличивает рейтинг команды при победе в турнире'''

        try:
            with sql.connect(self.database) as conn:
                self.team_name = self.lineEdit_2_tournert.text()
                if self.team_name.strip():
                    res = conn.cursor().execute(self.querry_found_tournier,(self.team_name,))
                    for row in res:
                        new= row[0]
                        new += 1
                        res = conn.cursor().execute(self.update_tournier,(new,self.team_name))
                        result = QMessageBox()
                        result.setText(f'Рейтинг команды {self.team_name} обновлен')
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


    