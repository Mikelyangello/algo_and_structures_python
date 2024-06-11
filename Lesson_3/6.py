"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""


def gen_random_int():
    import random
    num_sign = int(random.random()*100)
    num_sign = -1 if num_sign < 50 else 1
    return int(random.random()*100)*num_sign


size_of_massive = int(input("Введите размер массива: "))
massive = [gen_random_int() for i in range(size_of_massive)]
print(massive)


def search_min_max(mass, cur_i=0, min_i=0, max_i=0):
    if cur_i == len(mass):
        return min_i, max_i
    if mass[cur_i] < mass[min_i]:
        return search_min_max(mass, cur_i+1, cur_i, max_i)
    elif mass[cur_i] > mass[max_i]:
        return search_min_max(mass, cur_i+1, min_i, cur_i)
    else:
        return search_min_max(mass, cur_i+1, min_i, max_i)


result = sorted(search_min_max(massive))
print(sum(massive[result[0]+1:result[1]:]))
