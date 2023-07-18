''' Вывод и удаление вопросов из базы'''

import sqlite3 as sql
conn = sql.connec('New_Brain_base')
cursor = conn.cursor()
cursor.execut('SELECT brain_base_id, вопрос FROM brain_base LIMIT 1 WHERE комментарий LIKE input() ORDER BY уровень')
row = cursor.fetchone()
print(row)
conn.close()


num = brain_base_id

conn = sql.connect('New_Brain_base')
cursor = sql.connect.cursor
cursor.execut('DELETE FROM brain_base WHERE brain_base_id = num ')
conn.commit()