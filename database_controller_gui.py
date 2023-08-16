from typing import Self, TextIO
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget
import sys
from PyQt6 import *
import sqlite3 as sql
from openpyxl import load_workbook
import logging as log
from PyQt6.QtSql import  QSqlDatabase, QSqlQuery
from PyQt6.QtCore import *
from dataface import *




class Controller(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.Connect.clicked.connect(self.get_connection)
        self.Load_exel.clicked.connect(self.add_questions_from_excel)
        self.new_qwestion.text()
        self.new_answer.text()
        self.Load_new.clicked.connect(self.add_single_question)
        self.Update_question.text()
        self.Update_answer_2.text()
        self.foungQ.text()
        self.foundAns.text()
        self.UpdatEQ.clicked.connect(self.update_question)
        self.sellect_all.clicked.connect(self.get_all_questions)
        self.Del_qwestion.text()
        self.pushButton.clicked.connect(self.delete_question)
        self.count_added_questions = 0
        self.query_add_single_question = '''INSERT INTO questions (question, answer) VALUES (?, ?)'''     # Запрос на добавление записи в БД
        self.query_get_all_questions = '''SELECT * FROM questions'''
        self.query_get_single_question = '''SELECT question, answer FROM questions WHERE question LIKE ? OR answer LIKE ?'''
        self.query_update_question = '''UPDATE questions SET question = ? WHERE question LIKE ?'''
        self.query_update_answer = '''UPDATE questions SET answer = ? WHERE answer LIKE ?'''
        self.query_delete_question = '''DELETE FROM questions WHERE question LIKE ? OR answer LIKE ?'''
        self.foubd_question = ''
        self.database = 'app/assets/database/brainring.db'
        self.excel_file = 'app/assets/database/questions_template.xlsx'    # Имя файла-шаблона, при загрузке через интерфейс - указывать путь выбранному файлу
        self.conn = None

    def get_connection(self):
        ''' Функция осуществляет подключение к базе данных database '''
        log.debug("==> get_connection() - функция вызвана.\n")
        conn = sql.connect(self.database)
        if conn:
            result =  QMessageBox()
            result.setText('Cоединение создано')
            result.exec()
        else:
            result =  QMessageBox()
            result.setText('Не удалось подключиться к базе')
            result.exec()
           
# ----------------------------------------------------------- #

    def get_all_questions(self):
        '''Функция выводит все вопросы и ответы в таблицу'''
        with sql.connect(self.database ) as conn:
            result = conn.cursor().execute(self.query_get_all_questions).fetchall()
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(len(result[0]))
            for row in range(len(result)):
                for column in range(len(result[row])):
                    item = QTableWidgetItem(result[row][column])
                    self.tableWidget.setItem(row,column,item)
        

# ----------------------------------------------------------- #

    def get_single_question(self):
        ''' Функция возвращает из базы данных один вопрос, в котором есть соответствующий текст эта функция не привязана к виджетам'''
        log.debug("==> get_single_question() - функция вызвана.\n")
        with sql.connect(self.database) as conn:
            found_answer =self.foundAns.text() #Проверяем ввел ли пользователь данные
            found_question = self.foungQ.text()
            result = conn.cursor().execute(self.query_get_all_questions).fetchall()
            for row in result:
                if found_question == row[1] or found_answer == row[2]: #проверяем наличие вопроса в базе
                    print('Вопрос найден')
                else:
                    log.warning("<== Вопрос (ответ) не найден в БД.\n")
                    print('Вопрос не найден')
                    # WARNING - исправить на случай если вопросы не найдены, чтобы не было ошибки
                
        
# ----------------------------------------------------------- #

    def add_single_question(self):
        ''' Добавление одного вопроса'''
        log.debug("> add_single_question() - функция вызвана.\n")
     
        with sql.connect(self.database) as conn: 
            cursor = conn.cursor()
            new_question =  self.new_qwestion.text()
            new_answer = self.new_answer.text()
            if new_question.strip() and new_answer.strip(): #Проверяем ввел ли пользоваетель данные
                cursor.execute(self.query_add_single_question, (new_question, new_answer))
                self.count_added_questions += 1
                result =  QMessageBox()
                result.setText('Вопрос добавлен')
                result.exec()
                   
            else:
                log.warning("< Поле  не может быть пустым!\n")
                result =  QMessageBox()
                result.setText('Поля не заполнены')
                result.exec()
                log.debug("< add_single_question() - конец выполнения.\n")
            
# ----------------------------------------------------------- #

    def add_questions_from_excel(self):
        ''' Добавление вопросов из Excel-файла. '''
        log.debug("==> add_questions_from_excel() - функция вызвана.\n")
        self.count_added_questions = 0
        # ДОБАВИТЬ: проверку расширения файла excel; продумать, на каком этапе её лучше делать

          # Попытка открыть файл
        workbook = load_workbook(self.excel_file)  # Загружаем Excel-файл
        sheet = workbook['page']    # Указываем название страницы (можно ли переделать на индекс?)'
           
        self.count_added_questions = 0 # Обнуление добавленных вопросов
        if sheet["A1"].value == "Вопрос" and sheet["B1"].value == "Ответ":
            for row in sheet.iter_rows(min_row=2, values_only=True):
                with sql.connect(self.database) as conn:
                    cursor = conn.cursor()
                    cursor.execute(self.query_add_single_question, (row[0], row[1]))
            result =  QMessageBox()
            result.setText('Вопросы добавлены')
            result.exec()
        else:
            result =  QMessageBox()
            result.setText('Файл не соответствует формату')
            result.exec()
                   
# ----------------------------------------------------------- #

    def update_question(self):
        ''' Функция изменяет текст вопроса и ответа для вопроса с идентификатором question_id'''
        log.debug("> update_question() - функция вызвана.\n")
        with sql.connect(self.database) as conn:
            try: # Пытаемся выполнить запрос по изменению вопроса в БД
                upd_question= self.Update_question.text() #Проверяем ввел ли пользователь данные
                upd_answer =  self.Update_answer_2.text()
                found_question = self.foungQ.text()
                found_answer = self.foundAns.text()
                if upd_question.strip()  and upd_answer.strip() and found_question.strip() and found_answer.strip():
                    result = conn.cursor().execute(self.query_get_single_question,(found_question,found_answer))
                    if result:
                        conn.cursor().execute(self.query_update_question,(upd_question,found_question))
                        conn.cursor().execute(self.query_update_answer,(upd_answer,found_answer))
                        result =  QMessageBox()
                        result.setText('Вопрос\ответ изменен')
                        result.exec()
                        
                    else:
                        result =  QMessageBox()
                        result.setText('Ошибка при изменении вопроса')
                        result.exec()
                        
                else:
                    result =  QMessageBox()
                    result.setText('Изменяемый вопрос  не найден')
                    result.exec()
                   
            except Exception as e:
                log.warning(f"< Ошибка при изменении вопроса: {e}\n")

        
# ----------------------------------------------------------- #

    def delete_question(self):
        ''' Функция удаляет строку с поиском по вопросу или ответу'''
        log.debug("> delete_question() - функция вызвана.\n")
        with  sql.connect(self.database) as conn:
            del_question  = self.Del_qwestion.text()
            del_answer = self.del_answer.text()
            if del_question.strip() and del_answer.strip():
               result = conn.cursor().execute(self.query_get_single_question,(del_question,del_answer))
               if result:
                    conn.cursor().execute(self.query_delete_question,(del_question,del_answer))
                    res = 'вопрос успешно удален'
               else:
                    res = 'Заполнены не все поля или вопрос никогда не сущестовал'
            result =  QMessageBox()
            result.setText(res)
            result.exec()
        
# ----------------------------------------------------------- #

log.debug("===== Конец выполнения файла database_controller.py. =====")


    
  
app = QApplication(sys.argv)
window = Controller()
sys.exit(app.exec())
