import sqlite3 as sql
conn = sql.connect('New_Brain_base')
cur = conn.cursor()
result = cur.execute('select * from brain_base;')
result = cur.fetchone()
querry = 'insert into brein_base(вопрос, ответ, комментарий, уровень) values (input(),input(),input, int(input(), NULL, NULL);'
count = cur.execute(querry)
conn.commit()
cur.close()