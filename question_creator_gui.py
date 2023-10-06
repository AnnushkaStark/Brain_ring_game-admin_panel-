from typing import Self, TextIO
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget
import sys
from PyQt6 import *
import sqlite3 as sql
from question_creator import *



class Creator(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.spinBox_limit.setValue(0)
        self.pushButton_back_2.clicked.connect(self.question)
        self.pushButton_submit.clicked.connect(self.submit)
        self.plainTextEdit.setPlainText('')
    
    def submit(self):
        pass



    def question(self):
        pass


