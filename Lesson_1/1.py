# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

digit = int(input('Введите трехзначное число: '))
a = digit % 10
b = (digit - a) / 10 % 10
c = (digit - a - b * 10) / 100 % 10
result_summ = a + b + c
result_mult = a * b * c
print(f'Ваше число {digit}, имеет следующие результаты:\n'
      f'- по сумме цифр {result_summ:.0f}\n'
      f'- по их произведению {result_mult:.0f}')

# Второй способ решения
digit = input('Введите трехзначное число: ')
a = int(digit[0])
b = int(digit[1])
c = int(digit[2])
result_summ = a + b + c
result_mult = a * b * c
print(f'Ваше число {digit}, имеет следующие результаты:\n'
      f'- по сумме цифр {result_summ:.0f}\n'
      f'- по их произведению {result_mult:.0f}')
