"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


def output(code=32, text='', counter=0):
    if code == 128:
        if text != '':
            print(text)
        return
    if counter == 10:
        print(text)
        text = ''
        counter = 0
    text += f'{code}-{chr(code)}  '
    code += 1
    counter += 1
    return output(code, text, counter)


output()
