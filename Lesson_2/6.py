"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""

from random import random

min_number = 0
max_number = 100


def random_number(min, max):
    return int(random() * (max - min + 1))


def extrasens(counter=1, secret_number=None):
    if secret_number is None:
        return extrasens(secret_number=random_number(min_number, max_number))
    if counter == 11:
        return print(f'К сожалению, вы проиграли. Загаданное число: {secret_number}')
    user_answer = int(input(f'Попытка №{counter}\nВведите число: '))
    if user_answer == secret_number:
        return print(f'Поздравляем! Вы отгадали число {secret_number} с {counter} попыток')
    elif user_answer > secret_number:
        print('Загаданное число меньше')
    else:
        print('Загаданное число больше')
    counter += 1
    return extrasens(counter, secret_number)

extrasens()