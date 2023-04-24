import time
from SQLite.db_handlers import *
import sqlite3 as sql

while True:
    print('Если вы хотите добавить вопрос, введите: "add".')
    print('Если вы хотите просмотреть имеющиеся вопросы, введите: "show".')
    print('Если вы хотите изменить какой-то вопрос, введите: "edit".')
    print('Если вы хотите удалить вопрос, введите: "delete".')
    print('Если вы хотите закрыть модуль, введите: "exit".')
    choise = input()
    if choise=='exit':
        break
    elif choise=='add':
        add_question()
    elif choise == 'show':
        show_question()
    elif choise == 'edit':
        pass
    elif choise == 'delete':
        delete_question()
    else:
        pass