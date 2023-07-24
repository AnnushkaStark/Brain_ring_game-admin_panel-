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
query_get_single_question = '''SELECT question, answer FROM questions WHERE question LIKE ? OR answer LIKE ?'''
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
    ''' Функция возвращает из базы данных один вопрос, в котором есть соответствующий текст'''
    log.debug("==> get_single_question() - функция вызвана.\n")
    with get_connection() as conn:
        try:
            result = conn.cursor().execute(query_get_single_question, ('%' + text + '%', '%' + text + '%')).fetchone()
            if result:
                log.debug("<== get_single_question() - конец выполнения.\n")
                return result
            else:
                log.warning("<== Вопрос (ответ) не найден в БД.\n")
                # WARNING - исправить на случай если вопросы не найдены, чтобы не было ошибки
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

def update_question(question_id: int, new_question: str, new_answer: str):
    ''' Функция изменяет текст вопроса и ответа для вопроса с идентификатором question_id'''
    with get_connection() as conn:
        conn.cursor().execute('UPDATE questions SET question = ?, answer = ? WHERE id == ?', (new_question, new_answer, question_id))

# ----------------------------------------------------------- #

def delete_question(delete_question_id):
    ''' Функция удаляет строку с поиском по вопросу или ответу'''
    with get_connection() as conn:
        # Проверяем наличие строки  в таблице
        row = conn.cursor().execute('DELETE FROM questions WHERE id == ?', (delete_question_id)).fetchone()
        if row is None:
            print('Вопрос не найден в базе данных')
        else:
            conn.cursor().execute("DELETE FROM questions WHERE id == ?", (delete_question_id))  # Удаляем строку
        print('Строка успешно удалена')
        
# ----------------------------------------------------------- #


# def delete_question(question: str):
#     pass

''' NEED REVIEW '''

def get_answer(update_answer):
    '''Функция выбирает ответ для обновления'''
    with get_connection() as conn:
        result = conn.cursor().execute('SELECT answer FROM questions WHERE answer == ?', (update_answer)).fetchone()
    if result is not None:
        return result
    else:
        return 'Ответ в базе не найден'

log.debug("===== Конец выполнения файла database_controller.py. =====")
