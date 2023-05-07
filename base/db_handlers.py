import sqlite3 as sql

conn = sql.connect('test')

cur = conn.cursor()
#в sqlite studio я подключился к этой БД
# и добавил туда одну колонку с наванием test1 типом данных текст а потом добавил туда данные "123"

result = cur.execute('select * from test;')
result = cur.fetchone()

#далее я через код добавляю данные в таблицу
querry = 'insert into test (test1) values (321);'
count = cur.execute(querry)
conn.commit()

#далее я получаю данные из таблицы, тут может быть много значний 321 ибо я пока разбирался надобавлял кучу
result = cur.execute('select * from test;')
for raw in result:
    print(raw)

#удаляю объект cur
cur.close()

