from typing import Self, TextIO
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget
import sys
from PyQt6 import *
import sqlite3 as sql
from question_creator import *
import random



class Creator(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.spinBox_limit.setMaximum(100)
        self.spinBox_limit.setMinimum(0)
        self.spinBox_limit.valueChanged.connect(self.questions_counter)
        self.pushButton_back_2.clicked.connect(self.question)
        self.pushButton_submit.clicked.connect(self.submit)
        self.plainTextEdit.setPlainText('')
        self.questions = []
        self.database = 'app/assets/database/brainring.db'
        self.select_all = '''SELECT question , answer FROM questions'''
        self.value = 0

    def questions_counter(self,value):
        '''Эта функция дает возможность выбрать количество вопросов для игры'''
        try:
            self.value = value
            return self.value
        except ValueError:
            res = QMessageBox()
            res.setText('Error')
            res.exec()

    
    def submit(self):
        '''Эта функция проверяет достаточно ли в таблице ворпосов для игры'''
        try:
            with sql.connect(self.database)as conn:
                res = conn.cursor().execute(self.select_all,).fetchall()
                if self.value > len(res):
                    result = QMessageBox()
                    result.setText('Превышен лимит выборки')
                    result.exec()
                else:
                    for _ in range(self.value +1):
                        self.questions.append(random.choice(res))

                    result = QMessageBox()
                    result.setText('Вопросы  отобраны')
                    result.exec()
                    return self.questions
                     
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



    def question(self):
        '''Эта функция выводит отобранные вопросы в игру'''
        try:
            if len(self.questions) == 0:
                result = QMessageBox()
                result.setText('Вопросы закончились')
                result.exec() 
            for row in self.questions:
                    self.plainTextEdit.setPlainText(f'вопрос : {row[0]} \n  ответ : {row[1]}')
                    self.questions.remove(row)
               
                    
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
            
       


