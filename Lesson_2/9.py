"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


numbers = input('Введите натуральные числа для проверки: ').split(' ')

def best_of_number(number, counter, summ):
    if type(number) is list:
        print('OK')

print(type(numbers))