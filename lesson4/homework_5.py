# 5.	Дано четырёхзначное число. Проверить, одинаковы ли все цифры в нём.


number = int(input('Введите четырёхзначное число: '))
number_1 = number // 1000
number_2 = number // 100 % 10
number_3 = number // 10 % 10
number_4 = number % 10

if number_1 == number_2 and number_2 == number_3 and number_3 == number_4:
    print('Все цифры одинаковые')
else:
    print('Цифры не одинаковые')
