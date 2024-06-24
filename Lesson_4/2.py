"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""


diapazon = list(range(2, int(input("Введите размер диапазона поиска простых чисел: ")) + 1))
ind = int(input("Введите номер индекса для нахождения i-го по счёту простого числа: ")) - 1


def rec_with_eratosfen(diap: list, indx: int, cur=2):
    if cur * 2 > diap[-1]:
        return print(f"Список простых чисел:\n{diap}\nв нем {indx} по счету простое число: {diap[indx]}")
    diap = [i for i in diap if i not in list(range(cur * 2, diap[-1] + 1, cur))]
    return rec_with_eratosfen(diap,
                              indx,
                              diap[diap.index(cur) + 1],
                              )


rec_with_eratosfen(diapazon, ind)
