"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

import collections


hex_digits = '0123456789ABCDEF'
numbers = collections.defaultdict(list)
result = collections.defaultdict(list)

for i in range(2):
    numbers[i].append(list(input(f'Введите {i+1}е число в 16 СС, например DE2A: ').upper()))

for i in range(2):
    print(len(numbers.values()))
