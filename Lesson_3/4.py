# 4.	Определить, какое число в массиве встречается чаще всего.


def gen_random_int():
    import random
    num_sign = int(random.random()*100)
    num_sign = -1 if num_sign < 50 else 1
    return int(random.random()*100)*num_sign


size_of_massive = int(input("Введите размер массива: "))
massive = [gen_random_int() for i in range(size_of_massive)]
print(massive)


def counter_in_mass(mass, cur_i=0, number=0, max_count=0):
    if cur_i == len(mass):
        return print(f"Максимальное количество раз ({max_count}) в массиве встречается число {number} ")
    if mass.count(mass[cur_i]) > max_count:
        return counter_in_mass(mass, cur_i+1, mass[cur_i], mass.count(mass[cur_i]))
    return counter_in_mass(mass, cur_i+1, number, max_count)


counter_in_mass(massive)
