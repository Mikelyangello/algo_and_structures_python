"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

number = int(input('Введите номер элемента:\n'))


def summ_of_elements(n, summ=0):
    if n == 0:
        return print(f'сумма элементов ряда чисел до элемента №{number} равна: {summ}')
    summ += 1 / (2 ** (n - 1)) - 2 / (2 ** (n - 1)) * ((n - 1) % 2)
    n -= 1
    return summ_of_elements(n, summ)


summ_of_elements(number)
