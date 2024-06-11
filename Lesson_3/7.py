"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""


def gen_random_int():
    import random
    num_sign = int(random.random()*100)
    num_sign = -1 if num_sign < 50 else 1
    return int(random.random()*100)*num_sign


size_of_massive = int(input("Введите размер массива: "))
massive = [gen_random_int() for i in range(size_of_massive)]
print(massive)


def couple_of_min(mass, cur_i=0, min1_i=0, min2_i=None):
    if cur_i == len(mass):
        return print(f"2 наименьших элемента в массиве:\n{mass[min1_i]} [i] {min1_i}\n{mass[min2_i]} [i] {min2_i}")

    if min2_i is None:
        if cur_i != min1_i:
            if mass[cur_i] < mass[min1_i]:
                return couple_of_min(mass, cur_i+1, cur_i, min1_i)
            return couple_of_min(mass, cur_i+1, min1_i, cur_i)
        return couple_of_min(mass, cur_i+1, min1_i, min2_i)

    if mass[cur_i] < mass[min2_i]:
        if mass[cur_i] <= mass[min1_i]:
            return couple_of_min(mass, cur_i+1, cur_i, min1_i)
        return couple_of_min(mass, cur_i + 1, min1_i, cur_i)

    return couple_of_min(mass, cur_i+1, min1_i, min2_i)


couple_of_min(massive)
