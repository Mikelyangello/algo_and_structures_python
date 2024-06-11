"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""

nat = int(input('Введите любое натуральное число для проверки равенства: 1+2+...+n = n(n+1)/2: '))


def check_expression(n, left=0, counter=1):
    while counter <= n:
        return check_expression(n, left+counter, counter+1)
    return print(f'Равенство существует? {left == n * (n + 1) / 2:>40}')


check_expression(nat)
