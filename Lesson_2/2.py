"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

number = int(input('Введите натуральное число:\n'))

odd_count = 0
even_count = 0


def counter(n, odd_count, even_count):
    if n == 0:
        return print(f'Число {number} содержит {even_count} четных и {odd_count} нечетных цифр')
    if n % 10 % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    n = (n - n % 10) / 10
    return counter(n, odd_count, even_count)


counter(number, odd_count, even_count)
