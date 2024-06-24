"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

import cProfile
from timeit import timeit as t
import sys
sys.setrecursionlimit(6000)


def counter(n, i, od=0, ev=0):

    while i != 0:
        if i % 10 % 2 == 0:
            ev += 1
        else:
            od += 1
        i //= 10
    return f"Число {n} содержит {ev} четных и {od} нечетных цифр"


def another_counter(num, i, od=0, ev=0):

    while i != 0:
        if int(num[i-1]) % 2 == 0:
            ev += 1
        else:
            od += 1
        i -= 1
    return f"Число {num} содержит {ev} четных и {od} нечетных цифр"


def main():
    counter(int('244336633333333454535345453453453'), int('244336633333333454535345453453453'))
    another_counter('244336633333333454535345453453453', len('244336633333333454535345453453453'))


print(t("counter(int('244336633333333454535345453453453'), int('244336633333333454535345453453453'))", globals=globals()))
print(t("another_counter('244336633333333454535345453453453', len('244336633333333454535345453453453'))", globals=globals()))
cProfile.run(main())
