# ----------------------------------------------------------- #
# Данный файл содержит все необходимые функции для работы с   #
# базой данных.                                               #
# ----------------------------------------------------------- #

""" Импорт зависимостей """

import sqlite3 as sql
from openpyxl import load_workbook
import logging

''' Константы '''

database = 'brainring.db'       # Имя БД
workbook = 'questions_file.xlsx'

add_query = '''INSERT INTO questions (question, answer)     
               VALUES (?, ?)'''         # Запрос на добавление записи в БД


''' Функции '''

def connect_db():
    ''' Функция осуществляет подключение к базе данных database '''
    logging.info("Вызвана функция connect_db()")
    connection = sql.connect(database)

    try:
        cursor = connection.cursor()
    except:
        logging.error('Database connection error.')
        return
    finally:
        return connection, cursor
    
    logging.info("Функция connect_db() завершила работу.")

def get_cursor(connection):
    try:
        with connection.cursor() as cursor:
    except:
        logging("Function get_cursor() failed!")
    finally:
        connection.close()

def select_all_questions():
    '''функция выводит все строки из базы данных'''
    logging.info("Вызвана функция select_all_questions()")

    connection, cursor = connect_db(database)   # Подключаемся к БД

    cursor.execute('SELECT * FROM questions')
    row = cursor.fetchone()
    print(row)
    connection.commit()
    cursor.close()
    connection.close()
    logging.info("Функция select_all_questions() завершила работу.")

def add_questions_from_excel(file):
    ''' Добавление вопросов группой из Excel-файла. '''

    logging.info("Вызвана функция add_questions_from_excel()")

    connection, cursor = connect_db(database)   # Подключаемся к БД

    workbook = load_workbook(filename = file)  # Загружаем Excel-файл
    sheet = workbook['page']    # Указываем название страницы (можно ли переделать на индекс?)'

    count = 0
    # Проходим по списку вопросов и добавляем уникальные в БД
    if sheet.row[0][0] == "Вопрос" and sheet.row[0][1] == "Ответ": # Не работает
        for row in sheet.iter_rows(min_row=2, values_only=True):
            try:
                cursor.execute(add_query, (row[0], row[1]))
                print('OK')
            except:
                logging.warning("Вопрос, который пользователь попытался добавить, уже существует в базе данных.")
                print('Такой вопрос уже существует!')
                print(f'Вопрос: {row[0]}')
                print(f'Вопрос: {row[1]}')
                print()
                continue
            count += 1
    else:
        print("Используйте только шаблон предоставленный программой!")

    print('Уникальные вопросы добавлены')

    # Закрываем соединение с БД
    connection.commit()
    connection.close()
    logging.info(f"Завершена работа функции add_question_from_excel(). Добавлено {count}/{sheet.row.count()} вопросов.")


def add_single_question(database: str, question: str, answer: str):
    ''' Добавление вопросов по одному по одному.'''

    connection, cursor = connect_db(database)   # Подключаемся к БД

    question, answer = input("Введите вопрос: "), input("Введите ответ: ") # Строка временная, не нужна при работе через интерфейс

    try:
        if question != '' and answer != '':
            cursor.execute(add_query, (question, answer))   # Непосредственно выполнение запроса к БД
            print('OK')
        else:
            raise sql.IntegrityError
    except sql.IntegrityError:
        print('Вопрос или ответ не может быть пустым!')
    except OSError as e:
        print(e)
        print('Такой вопрос уже существует!')
        print(f'Вопрос: {question}')
        print(f'Вопрос: {answer}')
        print()

    print('Уникальные вопросы добавлены')

    # Закрываем соединение с БД
    connection.commit()
    connection.close()

def delete_question(question: str):
    pass

def edit_question(question: str):
    pass





''' КОД ОТ АНАСТАСИИ - NEED REVIEW '''




update_question = input()     #введите вопрос который хотите обновить
update_answer = input() #введите ответ который хотите обновить
#conn = sql.connect('BrainRing.db')
#cursor = conn.cursor()

'''Функция выбирает вопрос для обновления из базы данных'''
def get_question(update_question):
    conn = sql.connect('BrainRing.db')
    cursor = conn.cursor()
    cursor.execute('SELECT вопрос FROM qwestions WHERE вопрос == update_question')
    result = cursor.fetchone()
    if result is not None:
        return result
    else:
        return 'Вопрос в базе не найден'
    conn.close

'''Функция выбирает ответ для обновления'''
def get_answer(update_answer):
    conn = sql.connect('BrainRing.db')
    cursor = conn.cursor()
    cursor.execute('SELECT ответ FROM questions WHERE ответ == update_answer')
    result = cursor.fetchone()
    if result is not None:
        return result
    else:
        return 'Ответ в базе не найден'
    сonn.close()

new_question = input()    #введите новый вопроc
new_answer = input()      #введите новый ответ


def update_question(update_question, update_answer):
    '''Эта функция обновляет вопрос '''
    conn = sql.connect('BrainRing.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE questions SET вопрос,  WHERE вопрос == update_question,(new_question'))
    conn.commit()
    conn.close()

new_answer = input()  # введите новый ответ


def update_answer():
    '''Эта функция обновляет ответ'''
    conn = sql.connect('BrainRing.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE questions SET ответ,  WHERE ответ == update_answer,(new_answer'))
    conn.commit()
    conn.close()

del_question = input() #введите  вопрос который хотите удалить
del_answer =input()  #введите ответ который хотите удалит

def delete_question(del_question):
    '''Эта функция удаляет строку с поиском по вопросу'''
    conn = sql.connect('BrainRing.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM questions WHERE вопрос LIKE del_question')  # Проверяем наличие строки  в таблице
    row = cursor.fetchone()
    if row is None:
        print('Вопрос не найден в базе данных')
    else:
        cursor.execute("DELETE FROM questions WHERE вопрос LIKE del_question")  # Удаляем строку
        conn.commit()
        print('Строка успешно удалена')
    cursor.close()
    conn.close()



def delete_answer(del_answer):
    '''Эта функция удаляет строку с поиском по ответу'''
    conn = sql.connect('BrainRing.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM questions WHERE ответ LIKE del_answer') #Проверяем наличие строки  в таблице
    row = cursor.fetchone()
    if row is None:
        print('Ответ не найден в базе данных')
    else:
        cursor.execute("DELETE FROM questions WHERE ответ LIKE del_answer") #Удаляем строку
        conn.commit()
        print('Строка успешно удалена')
    cursor.close()
    conn.close()


name = input() #введите название базы данных

def select_all(name):
    '''Эта функция выводит все строки из базы данных'''
    conn = sql.connect('BrainRing.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM questions')
    row = cursor.fetchone()
    print(row)
    conn.commit()
    cursor.close()
    conn.close