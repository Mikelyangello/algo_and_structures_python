#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.


def gen_random_int():
    import random
    num_sign = int(random.random()*100)
    num_sign = -1 if num_sign < 50 else 1
    return int(random.random()*100)*num_sign


size_of_massive = int(input("Введите размер массива: "))
massive = [gen_random_int() for i in range(size_of_massive)]
print(massive)


def perestanovka(mass, cur_i=0, min_i=0, max_i=0):
    if cur_i == len(mass):
        mass[min_i], mass[max_i] = mass[max_i], mass[min_i]
        return mass
    if mass[cur_i] < mass[min_i]:
        return perestanovka(mass, cur_i+1, cur_i, max_i)
    elif mass[cur_i] > mass[max_i]:
        return perestanovka(mass, cur_i+1, min_i, cur_i)
    else:
        return perestanovka(mass, cur_i+1, min_i, max_i)


massive = perestanovka(massive)
print(massive)
