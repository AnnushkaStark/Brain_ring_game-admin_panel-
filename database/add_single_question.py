'''
Добавление вопросов в таблицу по одному из игры
Проверяется уникальность текста вопроса (именно вопроса, не ответа).
'''

import sqlite3 as sql
conn = sql.connect('brainring.db')
cursor = conn.cursor()

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

conn.commit()
conn.close()
