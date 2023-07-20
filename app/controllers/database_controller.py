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

def connect_db(database: str):
    ''' Функция осуществляет подключение к базе данных database '''

    connection = sql.connect(database)

    try:
        cursor = connection.cursor()
    except:
        logging.error('Database connection error.')
        return

    return connection, cursor


def add_questions_from_excel(database, file):
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
