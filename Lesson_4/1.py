"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""


import timeit

"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
"""


def summ_of_elements(n, summ=0):
    if n == 0:
        return summ
    summ += 1 / (2 ** (n - 1)) - 2 / (2 ** (n - 1)) * ((n - 1) % 2)
    n -= 1
    return summ_of_elements(n, summ)


def summ_of_elements_by_cycle(n):
    summ = 0
    while n > 0:
        summ += 1 / (2 ** (n - 1)) - 2 / (2 ** (n - 1)) * ((n - 1) % 2)
        n -= 1
    return summ


recursion = timeit.timeit('summ_of_elements(500)',
                          setup="from __main__ import summ_of_elements",
                          number=1000)
cycle = timeit.timeit('summ_of_elements_by_cycle(500)',
                      setup="from __main__ import summ_of_elements_by_cycle",
                      number=1000)
print(f'(при вход.данных = 500)\n'
      f'{recursion:.6f} - рекурсия\n'
      f'{cycle:.6f} - цикл\n'
      f'отношение = {(float(cycle)/float(recursion)*100):.0f}%')

'''

Сложность алгоритма линейная O(n)
Рекурсия проигрывает циклу в среднем в диапазоне 10-20%.

(при вход.данных = 5)
0.005160 - рекурсия
0.004814 - цикл
отношение = 93%

(при вход.данных = 50)
0.055709 - рекурсия
0.045625 - цикл
отношение = 82%

(при вход.данных = 500)
1.063535 - рекурсия
0.886004 - цикл
отношение = 83%

'''

