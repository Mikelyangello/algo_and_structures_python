#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

start_postition_alphabet = ord('a')
symbol_1 = ord(input(f'Введите первую букву:\n')) - start_postition_alphabet + 1
symbol_2 = ord(input(f'Введите вторую букву:\n')) - start_postition_alphabet + 1
if symbol_2 > symbol_1:
    result = symbol_2 - symbol_1 - 1
elif symbol_1 > symbol_2:
    result = symbol_1 - symbol_2 - 1
else:
    result = 0
print(f'Позиция первой буквы в алфавите: {symbol_1}\n'
      f'Позиция второй буквы в алфавите: {symbol_2}\n'
      f'Между ними букв: {result}\n')
