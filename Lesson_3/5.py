#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
def gen_random_int():
    import random
    num_sign = int(random.random()*100)
    num_sign = -1 if num_sign < 50 else 1
    return int(random.random()*100)*num_sign


size_of_massive = int(input("Введите размер массива: "))
massive = [gen_random_int() for i in range(size_of_massive)]
print(massive)


def search_max_neg(mass, cur_i=0, max_i=0):
    if cur_i == len(mass):
        return print(f"В массиве максимальный отрицательный элемент: {mass[max_i]} индекс {max_i}")
    max_i = max_i if mass[max_i] < 0 else cur_i
    if mass[max_i] < mass[cur_i] < 0:
        return search_max_neg(mass, cur_i+1, cur_i)
    return search_max_neg(mass, cur_i+1, max_i)


massive = search_max_neg(massive)
print(massive)
