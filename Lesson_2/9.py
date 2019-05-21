"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


numbers = input('Введите натуральные числа для проверки: ').split(' ')


def summer(number, summ):
    if number == 0:
        return summ
    summ += number % 10
    return summer(number // 10, summ)


def best_of_number(numbers):
    result = 0
    max = 0
    for i in numbers:
        max_summ = summer(int(i), 0)
        if max_summ > result:
            result = max_summ
            max = i
    return print(f'Максимальная сумма: {result} у числа: {max}')


best_of_number(numbers)
