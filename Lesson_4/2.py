"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""


import timeit


def wrap_eratosfen(end, n=None):
    if n is None:
        n = end

    def eratosfen(m):
        erat_arr = list(range(m * 2))
        erat_arr[1] = 0
        for i in erat_arr:
            if i > 1:
                for j in range(i + i, len(erat_arr), i):
                    erat_arr[j] = 0
        return erat_arr

    result_arr = eratosfen(n)
    count_of_just_numbers = len(result_arr) - result_arr.count(0)
    if count_of_just_numbers < end:
        n += 1
        return wrap_eratosfen(end, n)
    else:
        counter = 1
        for i in result_arr:
            if i != 0:
                if counter == end:
                    return i
                counter += 1


def wrap_cycle(end, n):
    def cycle(n):
        lst = []
        for i in range(2, n + 1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                lst.append(i)
        return lst
    while len(cycle(n)) < end:
        n += 1
    return cycle(n).pop()


print(timeit.timeit("wrap_eratosfen(10)", setup="from __main__ import wrap_eratosfen", number=100))
print(timeit.timeit("wrap_cycle(10, 2)", setup="from __main__ import wrap_cycle", number=100))


'''
Решето работает быстрее в любых случаях, как при маленьких, так и при больших числах
Связано это с тем, что решето использует умный алгоритм и не перебирает все возможные комбинации цифр.
Замеры (всегда в количестве 100 запусков):

end = 4
0.00037033401895314455
0.001708939002128318
Решето быстрее на 78%

end = 40
0.1285964669950772
1.5947898809972685
Решето быстрее на 92%

end = 100
1.4070781960035674
31.90297833798104
Решето быстрее на 96%

Предполагаю, что сложность линеарифметическая - O(N log N)
'''