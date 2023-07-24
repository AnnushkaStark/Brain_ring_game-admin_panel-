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
log.info("========== Файл database_controller.py ==========")

database = 'app/database/brainring.db'           # Имя БД
excel_file = 'app/database/questions_template.xlsx'    # Имя файла-шаблона, при загрузке через интерфейс - указывать путь выбранному файлу

# -------------------------- Запросы ------------------------ #
query_add_single_question = '''INSERT INTO questions (question, answer) VALUES (?, ?)'''     # Запрос на добавление записи в БД
query_get_all_questions = '''SELECT * FROM questions'''
query_get_single_question = '''SELECT question, answer FROM questions WHERE question LIKE ? COLLATE NOCASE OR answer LIKE ? COLLATE NOCASE'''
query_update_question = '''UPDATE questions SET question = ?, answer = ? WHERE id = ?'''
query_delete_question = ''' '''

# -------------------------- ======= ------------------------ #
conn = None                         # Экземпляр соединения с БД
count_added_questions = 0           # Счётчик добавленных из excel-файла вопросов
# -------------------------- Функции ------------------------ #

def get_connection():
    ''' Функция осуществляет подключение к базе данных database '''
    log.debug("==> get_connection() - функция вызвана.\n")
    global conn
    if not conn:
        try:
            conn = sql.connect(database)
        except Exception as e:
            log.error(f"<== Не удалось подключиться к БД: {e}\n")
            raise
        finally:
            log.debug("<== Соединение с БД создано.\n")
    else:
        log.debug("<== Соединение с БД уже существует.\n")
    return conn

# ----------------------------------------------------------- #

def get_all_questions():
    ''' Функция возвращает все вопросы из базы данных '''
    log.debug("==> get_all_questions() - функция вызвана.\n")
    try:
        with get_connection() as conn:
            result = conn.cursor().execute(query_get_all_questions).fetchall()
            log.debug(f"Вопросов из БД получено - {len(result)} шт.")
        log.debug("<== get_all_questions() - конец выполнения. Связь с БД закрыта.\n")
        return result
    except Exception as e:
        log.error(f"<== Не удалось получить вопросы из базы данных: {e}\n")

# ----------------------------------------------------------- #

def get_single_question(text: str):
    ''' Функция возвращает один вопрос из базы данных '''
    log.debug("==> get_single_question() - функция вызвана.\n")
    with get_connection() as conn:
        try:
            result = conn.cursor().execute(query_get_single_question, ('%' + text + '%', '%' + text + '%')).fetchall()
            if result:
                log.debug("<== get_single_question() - конец выполнения.\n")
                return result
            else:
                log.warning("<== Вопрос (ответ) не найден в БД.\n")
                return 0, 0     # WARNING - исправить на случай если вопросы не найдены.
        except Exception as e:
            log.warning(f"<== Не удалось получить вопрос: {e}\n")
        
    
# ----------------------------------------------------------- #

def add_single_question(question, answer):
    ''' Добавление одного вопроса'''
    log.debug("> add_single_question() - функция вызвана.\n")
    global count_added_questions
    with get_connection() as conn:
        cursor = conn.cursor()
        try: # Пытаемся выполнить запрос по добавлению одного вопроса в БД
            if question == None:
                log.warning("< Поле 'Вопрос' не может быть пустым!\n")
            elif answer == None:
                log.warning("< Поле 'Ответ' не может быть пустым!\n")
            else:
                cursor.execute(query_add_single_question, (question, answer))
                count_added_questions += 1
                log.debug("< add_single_question() - конец выполнения.\n")
        except sql.IntegrityError as sql_error:
            log.warning(f"< Вопрос уже существует в базе данных: {sql_error.args}\n")
        except Exception as e:
            log.warning(f"< Ошибка при добавлении вопроса: {e}\n")

# ----------------------------------------------------------- #

def add_questions_from_excel(file):
    ''' Добавление вопросов из Excel-файла. '''
    log.debug("==> add_questions_from_excel() - функция вызвана.\n")
    global count_added_questions
    # ДОБАВИТЬ: проверку расширения файла excel; продумать, на каком этапе её лучше делать

    try:    # Попытка открыть файл
        workbook = load_workbook(filename = file)  # Загружаем Excel-файл
        sheet = workbook['page']    # Указываем название страницы (можно ли переделать на индекс?)'

        count_added_questions = 0 # Обнуление добавленных вопросов
        if sheet["A1"].value == "Вопрос" and sheet["B1"].value == "Ответ":      # Проверка на соответствие загружаемого файла шаблону
            for row in sheet.iter_rows(min_row=2, values_only=True):
                log.debug(f"Обрабатывается строка: {row}")
                add_single_question(row[0], row[1])
            log.debug(f"<== add_question_from_excel() - конец выполнения. Добавлено {count_added_questions}/{sheet.max_row - 1} вопросов.\n") 
        else:
            log.error("<== Попытка использовать файл, не соответствующий шаблону!\n")
    except Exception as e:
        log.error(f"<== Невозможно открыть excel-файл: {e}\n")
        
# ----------------------------------------------------------- #

# ----------------------------------------------------------- #
# ----------------------------------------------------------- #
# ----------------------------------------------------------- #


# def delete_question(question: str):
#     pass

def edit_question(question: str):
    pass





''' NEED REVIEW '''

'''Функция выбирает вопрос для обновления из базы данных'''


'''Функция выбирает ответ для обновления'''
def get_answer(update_answer):
    conn = sql.connect('BrainRing.db')
    cursor = conn.cursor()
    cursor.execute('SELECT ответ FROM questions WHERE ответ == update_answer')
    result = cursor.fetchone()
    conn.close()
    if result is not None:
        return result
    else:
        return 'Ответ в базе не найден'
    

new_question, new_answer  = '', ''

def update_question(update_question, update_answer):
    '''Эта функция обновляет вопрос '''
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE questions SET вопрос,  WHERE вопрос == update_question',(new_question))
        conn.commit()

def update_answer():
    '''Эта функция обновляет ответ'''

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE questions SET answer,  WHERE answer == update_answer', (new_answer))
        conn.commit()
        cursor.close()

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

log.debug("===== Конец выполнения файла database_controller.py. =====")
