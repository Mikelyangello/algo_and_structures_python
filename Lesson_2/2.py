"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

number = input('Введите натуральное число:\n')


def counter(n, i, od=0, ev=0):
    if i == 0:
        return print(f'Число {n} содержит {ev} четных и {od} нечетных цифр')
    if i % 10 % 2 == 0:
        return counter(n, i // 10, od, ev + 1)
    else:
        return counter(n, i // 10, od + 1, ev)


counter(int(number), int(number))


def another_counter(num, i, od=0, ev=0):
    if i == 0:
        return print(f"Число {num} содержит {ev} четных и {od} нечетных цифр")
    if int(num[i-1]) % 2 == 0:
        return another_counter(num, i - 1, od, ev + 1)
    else:
        return another_counter(num, i - 1, od + 1, ev)


another_counter(number, len(number))
