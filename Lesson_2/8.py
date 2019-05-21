"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""


n = int(input("Введите искомую цифру: "))
limit = int(input("Сколько будет чисел в последовательности: "))
counter = 0


def searcher(number, digit, entries=0):
    if number == 0:
        return entries
    if number % 10 == digit:
        entries += 1
    return searcher(number // 10, digit, entries)


for i in range(limit):
    temp = int(input(f'Введите число #{i + 1}(из {limit}) последовательности: '))
    counter = searcher(temp, n, counter)


print(f'Искомое число в последовательности встречается раз: {counter}')
