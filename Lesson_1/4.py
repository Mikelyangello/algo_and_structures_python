"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""
from random import random

quest_delimetr = '-'*120
text_min = 'Введите минимальную границу диапазона '
text_max = 'Введите максимальную границу диапазона '
text_digits = 'чисел: '
text_symbols = 'букв: '

# -------------------------------------------------------------------
# Часть 1. Вывод случайного целого числа из заданного дипазона
quest_text = f'\n{quest_delimetr}\nЧасть 1. Вывод случайного целого числа из заданного дипазона'
print(quest_text)
digit_1 = int(input(f'{text_min}{text_digits}'))
digit_2 = int(input(f'{text_max}{text_digits}'))
if digit_2 > digit_1:
    result = int(random() * (digit_2 - digit_1 + 1) + digit_1)
elif digit_1 > digit_2:
    result = int(random() * (digit_1 - digit_2 + 1) + digit_2)
else:
    result = digit_1
print(f'Результат: {result}')


# -------------------------------------------------------------------
# Часть 2. Вывод случайного вещественного числа из заданного дипазона
quest_text = f'\n{quest_delimetr}\nЧасть 2. Вывод случайного вещественного числа из заданного дипазона'
print(quest_text)
digit_3 = float(input(f'{text_min}{text_digits}'))
digit_4 = float(input(f'{text_max}{text_digits}'))
if digit_4 > digit_3:
    result = random() * (digit_4 - digit_3) + digit_3
elif digit_3 > digit_4:
    result = random() * (digit_3 - digit_4) + digit_4
else:
    result = digit_3
print(f'Результат: {result}')

# -------------------------------------------------------------------
# Часть 3. Вывод случайного символа алфавита из заданного дипазона
quest_text = f'\n{quest_delimetr}\nЧасть 3. Вывод случайного символа алфавита из заданного дипазона'
print(quest_text)
symbol_1 = ord(input(f'{text_min}{text_symbols}'))
symbol_2 = ord(input(f'{text_max}{text_symbols}'))
if symbol_2 > symbol_1:
    result = int(random() * (symbol_2 - symbol_1 + 1) + symbol_1)
elif symbol_1 > symbol_2:
    result = int(random() * (symbol_1 - symbol_2 + 1) + symbol_2)
else:
    result = symbol_1
print(f'Результат: {chr(result)}')
