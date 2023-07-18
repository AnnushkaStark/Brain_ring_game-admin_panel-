import sqlite3 as sql

conn = sql.connect('New_Brain_base') #название базы данныъ

cur = conn.cursor()

result = cur.execute('select * from brain_base;') #название таблицы

for _ in result:
    print(_)
    print('---')