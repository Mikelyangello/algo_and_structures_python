"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
12f
da21
"""


import collections

hex_digits = '0123456789ABCDEF'
numbers = collections.defaultdict(list)

# заполняем словарь списками со значениями
for i in range(2):
    n = input(f'Введите {i+1}е число в 16 СС, например, DE2A: ').upper()
    for j in n:
        numbers[i].append(j)

decimals = list()

for k, v in numbers.items():
    n = 0
    for i in v:
        n += hex_digits.index(i) * (16 ** (len(v) - v.index(i) - 1))
    decimals.append(n)

result = list()
result.append(decimals[0] + decimals[1])
result.append(decimals[0] * decimals[1])

for i in result:
    temp = list()
    while i > 0:
        temp.append(hex_digits[i % 16])
        if i == 16:
            temp.append('1')
            break
        i //= 16
    temp.reverse()
    numbers['result'].append(temp)

print(f'Работа с числами {numbers[0]} и {numbers[1]}:\n'
      f'их сумма: {numbers["result"][0]}\n'
      f'их произведение: {numbers["result"][1]}')
