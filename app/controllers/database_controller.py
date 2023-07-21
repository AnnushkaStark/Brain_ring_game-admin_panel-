# ----------------------------------------------------------- #
# Данный файл содержит все необходимые функции для работы с   #
# базой данных.                                               #
# ----------------------------------------------------------- #

# -------------------- Импорт зависимостей ------------------ #
import sqlite3 as sql
from openpyxl import load_workbook
import logging as log

# ------------------------- Константы ----------------------- #
log.basicConfig(filename='brainring.log', level=log.DEBUG,
                format='%(asctime)s - %(levelname)s - %(message)s')

log.info("Начало выполнения файла database_controller.py.")
log.debug("Отладка.")
log.warning("Предупреждение.")
log.error("Ошибка!")
log.critical("Критическая ошибка!")

database = 'brainring.db'           # Имя БД
workbook = 'questions_file.xlsx'    # Имя файла-шаблона, при загрузке через интерфейс - указывать путь выбранному файлу
add_query = '''INSERT INTO questions (question, answer) VALUES (?, ?)'''     # Запрос на добавление записи в БД
conn = None                         # Экземпляр соединения с БД

# 0------------------------- Функции ------------------------ #

def get_connection():
    ''' Функция осуществляет подключение к базе данных database '''
    log.info("Вызвана функция connect_db()")
    global conn
    if not conn:
        try:
            conn = sql.connect(database)
        except Exception as e:
            log.error("Database connection error:", e)
            raise
    log.info("Функция get_connection() завершила работу.")
    return conn

# ----------------------------------------------------------- #

def add_questions_from_excel(file):
    ''' Добавление вопросов группой из Excel-файла. '''
    log.info("Вызвана функция add_questions_from_excel()")
    # ДОБАВИТЬ: проверку расширения файла excel; продумать, на каком этапе её лучше делать
    try:
        workbook = load_workbook(filename = file)  # Загружаем Excel-файл
        sheet = workbook['page']    # Указываем название страницы (можно ли переделать на индекс?)'

        count = 0 # Счётчик добавленных вопросов
        try:
            conn = get_connection()
            try:
                if sheet[0][0].value == "Вопрос" and sheet[0][1].value == "Ответ":      # Проверка на соответствие загружаемого файла шаблону
                    for row in sheet.iter_rows(min_row=2, values_only=True):
                        try:
                            cursor = conn.cursor()
                            cursor.execute(add_query, (row[0], row[1]))
                        except Exception as e:
                            log.warning("Вопрос, который пользователь попытался добавить, уже существует в базе данных.")
                            print('Такой вопрос уже существует!')
                            print(f'Вопрос: {row[0]}')
                            print(f'Ответ: {row[1]}')
                            print()
                            continue
                        count += 1
                else:
                    print("Используйте только шаблон предоставленный программой!")

                cursor = conn.cursor()
                cursor.execute(add_query)
            except Exception as e:
                pass

        except Exception as e:
            pass

        
    except Exception as e:
        log.error("Not able to load excel-file:", e)
        raise
    
 

    log.info(f"Завершена работа функции add_question_from_excel(). Добавлено {count}/{sheet.rows} вопросов.")
    return

    

    count = 0
    # Проходим по списку вопросов и добавляем уникальные в БД
    

    print('Уникальные вопросы добавлены')

    # Закрываем соединение с БД
    connection.commit()
    connection.close()
    












# def get_cursor(connection):
#     try:
#         with connection.cursor() as cursor:
#             pass
#     except:
#         logging("Function get_cursor() failed!")
#     finally:
#         connection.close()

def select_all_questions():
    '''функция выводит все строки из базы данных'''
    log.info("Вызвана функция select_all_questions()")

    connection = get_connection()   # Подключаемся к БД
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM questions')
    row = cursor.fetchone()
    print(row)
    connection.commit()
    cursor.close()
    connection.close()
    log.info("Функция select_all_questions() завершила работу.")


def add_single_question(database: str, question: str, answer: str):
    ''' Добавление вопросов по одному по одному.'''

    connection = get_connection()   # Подключаемся к БД
    cursor = connection.cursor()
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

# def delete_question(question: str):
#     pass

def edit_question(question: str):
    pass





''' NEED REVIEW '''




# update_question = input()     #введите вопрос который хотите обновить
# update_answer = input() #введите ответ который хотите обновить
# conn = sql.connect('BrainRing.db')
#cursor = conn.cursor()

'''Функция выбирает вопрос для обновления из базы данных'''
def get_question(update_question):
    conn = sql.connect('BrainRing.db')
    cursor = conn.cursor()
    cursor.execute('SELECT вопрос FROM questions WHERE вопрос == update_question')
    result = cursor.fetchone()
    if result is not None:
        return result
    else:
        return 'Вопрос в базе не найден'
    conn.close

'''Функция выбирает ответ для обновления'''
def get_answer(update_answer):
    conn = sql.connect('BrainRing.db')
    cursor = conn.cursor()
    cursor.execute('SELECT ответ FROM questions WHERE ответ == update_answer')
    result = cursor.fetchone()
    if result is not None:
        return result
    else:
        return 'Ответ в базе не найден'
    сonn.close()

new_question = '' #input()    #введите новый вопроc
new_answer = '' #input()      #введите новый ответ


def update_question(update_question, update_answer):
    '''Эта функция обновляет вопрос '''
    conn = sql.connect('BrainRing.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE questions SET вопрос,  WHERE вопрос == update_question',(new_question))
    conn.commit()
    conn.close()

# new_answer = input()  # введите новый ответ


def update_answer():
    '''Эта функция обновляет ответ'''
    conn = sql.connect('BrainRing.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE questions SET ответ,  WHERE ответ == update_answer',(new_answer))
    conn.commit()
    conn.close()

# del_question = input() #введите  вопрос который хотите удалить
# del_answer =input()  #введите ответ который хотите удалить

def delete_question(del_question):
    '''Эта функция удаляет строку с поиском по вопросу'''
    conn = sql.connect('BrainRing.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM questions WHERE вопрос LIKE del_question')  # Проверяем наличие строки  в таблице
    row = cursor.fetchone()
    if row is None:
        print('Вопрос не найден в базе данных')
    else:
        cursor.execute("DELETE FROM questions WHERE вопрос LIKE del_question")  # Удаляем строку
        conn.commit()
        print('Строка успешно удалена')
    cursor.close()
    conn.close()



def delete_answer(del_answer):
    '''Эта функция удаляет строку с поиском по ответу'''
    conn = sql.connect('BrainRing.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM questions WHERE ответ LIKE del_answer') #Проверяем наличие строки  в таблице
    row = cursor.fetchone()
    if row is None:
        print('Ответ не найден в базе данных')
    else:
        cursor.execute("DELETE FROM questions WHERE ответ LIKE del_answer") #Удаляем строку
        conn.commit()
        print('Строка успешно удалена')
    cursor.close()
    conn.close()


# name = input() #введите название базы данных

def select_all(name):
    '''Эта функция выводит все строки из базы данных'''
    conn = sql.connect('BrainRing.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM questions')
    row = cursor.fetchone()
    print(row)
    conn.commit()
    cursor.close()
    conn.close

log.info("Конец выполнения файла database_controller.py.")