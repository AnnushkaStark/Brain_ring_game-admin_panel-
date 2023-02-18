import sqlite3 as sql

conn = sql.connect('questions.db')

curs = conn.cursor()

curs.execute("""CREATE TABLE IF NOT EXISTS questions(
question_id INT PRIMARY KEY,
text TEXT,
answer TEXT,
comment TEXT,
level TEXT);
""")
conn.commit()

questions = [('0001', 'Согласно одной несерьезной новости, на открытии нового '
              'корпуса роддома президент... Что сделал? Ответьте двумя словами, начинающимися с одной и той же буквы.',
              'Перерезал пуповину','None','1' )]

curs.executemany("INSERT INTO questions VALUES(?, ?, ?, ?, ?);", questions)

curs.execute("""select * from questions""")

one_result = curs.fetchone()

print(one_result)