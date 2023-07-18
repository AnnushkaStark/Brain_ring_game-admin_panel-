import sqlite3 as sql
from openpyxl import load_workbook

''' Подключение к БД '''
connection = sql.connect('brainring.db')
try:
    cursor = connection.cursor()
except:
    print('Connection error')

'''
Добавление вопросов из Excel-файла
'''
workbook = load_workbook(filename = 'questions_file.xlsx')
sheet = workbook['page']

query = '''INSERT INTO questions(question, answer)
           VALUES(?,?)'''

if sheet.row[0][0] == "Вопрос" and sheet.row[0][1] == "Ответ": # Не работает
    for row in sheet.iter_rows(min_row=2, values_only=True):
        try:
            cursor.execute(query, (row[0], row[1]))
            print('OK')
        except:
            print('Такой вопрос уже существует!')
            print(f'Вопрос: {row[0]}')
            print(f'Вопрос: {row[1]}')
            print()
else:
    print("Используйте только шаблон предоставленный программой!")

print('Уникальные вопросы добавлены')
connection.commit()
connection.close()

'''
Добавление вопросов в таблицу по одному из игры
Проверяется уникальность текста вопроса (именно вопроса, не ответа).
'''

query = '''INSERT INTO questions (question, answer)
           VALUES (?, ?)'''

question, answer = input("Введите вопрос: "), input("Введите ответ: ")
try:
    if question != '' and answer != '':
        cursor.execute(query, (question, answer))   # Непосредственно выполнение запроса к БД
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

connection.commit()
connection.close()
