# 8.	Определить, является ли год, который ввел пользователем,
# високосным или не високосным.
#Год является високосным в двух случаях: либо он кратен 4,
# но при этом не кратен 100, либо кратен 400.

user_year = int(input('Введите год для проверки:\n'))
result = 'високосный'
if user_year % 400 == 0 or (user_year % 100 != 0 and user_year % 4 == 0):
    pass
else:
    result = 'не високосный'
print(f'год {user_year} - {result}')
