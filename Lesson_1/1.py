# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

digit = int(input('Введите трехзначное число: '))
a = digit % 10
b = digit // 10 % 10
c = digit // 100 % 10
result_summ = a + b + c
result_mult = a * b * c
print(f'Ваше число {digit}, имеет следующие результаты:\n'
      f'- по сумме цифр {result_summ:.0f}\n'
      f'- по их произведению {result_mult:.0f}')

# Второй способ решения через перебор списка
digit = input('Введите трехзначное число: ')
a = int(digit[0])
b = int(digit[1])
c = int(digit[2])
result_summ = a + b + c
result_mult = a * b * c
print(f'Ваше число {digit}, имеет следующие результаты:\n'
      f'- по сумме цифр {result_summ:.0f}\n'
      f'- по их произведению {result_mult:.0f}')

# Третий способ решения через цикл
digit = input('Введите трехзначное число: ')
result_summ = 0
result_mult = 1
for i in range(3):
      result_summ += int(digit[i])
      result_mult *= int(digit[i])
print(f'Ваше число {digit}, имеет следующие результаты:\n'
      f'- по сумме цифр {result_summ:.0f}\n'
      f'- по их произведению {result_mult:.0f}')

# Четвертый способ решения через класс
class Digit:
      """The class of symbols,
      that man insert"""

      def __init__(self, inp: str):
            self.inp = inp
            self.sum = self.get_sum()
            self.mul = self.get_mul()

      def get_sum(self):
            res = 0
            for i in range(len(self.inp)):
                  res += int(self.inp[i])
            return res


      def get_mul(self):
            res = 1
            for i in range(len(self.inp)):
                  res *= int(self.inp[i])
            return res

digit = Digit(input('Введите трехзначное число: '))
print(f'Ваше число {digit.inp}, имеет следующие результаты:\n'
      f'- по сумме цифр {digit.sum:.0f}\n'
      f'- по их произведению {digit.mul:.0f}')
