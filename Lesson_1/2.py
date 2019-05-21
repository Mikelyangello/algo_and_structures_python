# 2. Выполнить логические побитовые операции "И", "ИЛИ" и др.
# над числами 5 и 6. Выполнить
# над числом 5 побитовый сдвиг вправо и влево на два знака.

result_and = 5 & 6
result_or = 5 | 6
result_xor = 5 ^ 6
result_left_swipe = 5 << 2
result_right_swipe = 5 >> 2
result_inversion = ~5
print(f'результаты побитовых операций:\n'
      f'побитовое И.                  5 & 6: {result_and}\n'
      f'побитовое ИЛИ.                5 | 6: {result_or}\n'
      f'побитовое исключающее ИЛИ.    5 ^ 6: {result_xor}\n'
      f'побитовый сдвиг влево.        5 << 2: {result_left_swipe}\n'
      f'побитовый сдвиг вправо.       5 >> 2: {result_right_swipe}\n'
      f'побитовая инверсия.           ~5: {result_inversion}')
