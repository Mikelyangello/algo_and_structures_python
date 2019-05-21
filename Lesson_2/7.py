"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""

n = int(input('Введите любое натуральное число для проверки равенства: 1+2+...+n = n(n+1)/2: '))


def check_expression(n, left=0, counter=1):
    while counter <= n:
        left += counter
        counter += 1
        return check_expression(n, left, counter)
    return print(f'Равенство существует? {left == n * (n + 1) / 2}')


check_expression(n)
