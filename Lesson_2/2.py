"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

number = input('Введите натуральное число:\n')

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


counter(int(number), odd_count, even_count)

def another_counter(num, i, od=0, ev=0):
    if i==0:
        return print(f"Число {num} содержит {ev} четных и {od} нечетных цифр")
    if int(num[i-1]) % 2 == 0:
        ev += 1
    else:
        od += 1
    return another_counter(num, i-1, od, ev)


another_counter(number, len(number))
