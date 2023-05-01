import sys

from classes import questions
import time
from random import randint

print('For new game enter N')
cm = input()
if cm=='N':
    print('Внимание вопрос!', end='')
    time.sleep(2)
    print('\r', end='')
    print(questions[0].get_text(), end='')
    time.sleep(5)

print('\r', end='')
print('Время пошло!', end='')
time.sleep(1)
_ = 60
while _ > 0:
    print('\r', end='')
    print(f'{str(_)}', end='')
    _-=1
    time.sleep(1)

print('\r', end='')
print(f'Ваш ответ?')

cm = input()

print('\r', end='')
print(f'Правильный ответ: {questions[0].get_answer()}')




