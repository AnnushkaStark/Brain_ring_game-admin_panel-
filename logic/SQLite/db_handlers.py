import sqlite3 as sql
import time

conn = sql.connect('questions.db')
curs = conn.cursor()
curs.execute("""CREATE TABLE IF NOT EXISTS questions(
question_id INTEGER PRIMARY KEY AUTOINCREMENT,
text TEXT,
answer TEXT,
comment TEXT,
level TEXT);
""")
conn.commit()

#print(one_result)
def add_question():
    print(' ')
    print('If you whant to add data from .csv file - enter \'csv\'')
    print('If you whant to add data manual - enter \'manual\'')
    print(' ')
    choise = input()
    if choise == 'csv':
        pass #TODO написать ввод из цсв
    elif choise == 'manual':
        while True:
            print('Enter text of a question:')
            text1 = input()
            print('Enter answer of a question:')
            answer1 = input()
            print('Enter comment to question:')
            comment1 = input()
            print('Enter level of a question:')
            level1 = input()
            print('OK!')
            time.sleep(1)
            print('You etnered next values:')
            print('Question text is:')
            print(text1)
            time.sleep(1)
            print('Answer to question is:')
            print(answer1)
            time.sleep(1)
            print('Comment to question is:')
            print(comment1)
            time.sleep(1)
            print('Question level is:')
            print(level1)
            time.sleep(1)
            print('Are you entered right values? (Y/N)')
            choise1 = input()
            if choise1 == 'Y':
                questions = [(text1, answer1, comment1, level1)]
                curs.executemany(f'INSERT INTO questions (text, answer, comment, level) VALUES(?, ?, ?, ?);', questions)
                conn.commit()
                curs.execute('select * from questions;')
                res = curs.fetchall()
                print(res)
                break
            else:
                pass
        else:
            pass

def show_question():
    curs.execute('select max(question_id) from questions;')
    size = str(curs.fetchone())
    size = size[1:-2]
    print(f'Количество вопросов в базе: {size}.')
    print('Если вы хотите посмотреть все, введите: "all".')
    print('Если знаете ID вопроса введите: "id - {id вопроса}.')

    curs.execute('select question_id from questions;')
    tmp1 = list()
    while True:
        res = curs.fetchone()
        # res = res[1:-2]
        if res:
            tmp1.append(res)
        else:
            break
    list_of_id = list()
    for x in tmp1:
        y = str(x)
        x = y[1:-2]
        list_of_id.append(x)

    choise2 = input()
    if choise2 == 'all':
        curs.execute('select * from questions;')
        while True:
            res = curs.fetchone()
            if res:
                print(f'id - {res[0]}.')
                print(f'question text - {res[1]}.')
                print(f'answer is - {res[2]}.')
                print(f'comment is - {res[3]}.')
                print(f'level is - {res[4]}.')
                print('---------------------------------------------')
                time.sleep(2)
            else:
                break
    elif choise2[5:] in list_of_id:
        curs.execute(f'select * from questions where question_id like {choise2[5:]}')
        res = curs.fetchone()
        if res:
            print('---------------------------------------------')
            print(f'id - {res[0]}.')
            print(f'question text - {res[1]}.')
            print(f'answer is - {res[2]}.')
            print(f'comment is - {res[3]}.')
            print(f'level is - {res[4]}.')
            print('---------------------------------------------')
            time.sleep(2)
    elif choise2[5:] not in list_of_id:
        print('Вопроса с таким айди нет в базе. Проверьте правильность введенных вами данных.')
        print('')
    else:
        print('Hm... something wrong? try again later.')

def delete_question():
    print('Введите id вопроса, который вы хотите удалить.')
    id_to_delete = input()
    curs.execute(f'select * from questions where question_id like {id_to_delete}')
    while True:
        res = curs.fetchone()
        if res:
            print(f'id - {res[0]}.')
            print(f'question text - {res[1]}.')
            print(f'answer is - {res[2]}.')
            print(f'comment is - {res[3]}.')
            print(f'level is - {res[4]}.')
            print('---------------------------------------------')
            time.sleep(2)
        else:
            break
    print('Это нужный вам вопрос? (Y/N)')
    choise = input()
    if choise == 'Y':
        curs.execute(f'delete from questions where question_id = {id_to_delete}')
    elif choise == 'N':
        delete_question()
    else:
        print('Hm. something wrong, try again...')
        delete_question()