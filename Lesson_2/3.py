"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

number = int(input('Введите натуральное число:\n'))


def reformator(n, un_number=0):
    if n == 0:
        return print(f'Число: {number} наоборот: {un_number}')
    if un_number == 0:
        un_number = n % 10
    else:
        un_number = int(f'{un_number}{n % 10}')
    n = int((n - n % 10) / 10)
    return reformator(n, un_number)


reformator(number)
