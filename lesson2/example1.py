#Задание создать переменную типа строка и преобразовать ее в число.

example_string = input('Введите число: ')

try:
    int_string = int(example_string)
    if int_string:
        print(f'Вы ввели число {int_string}')
except ValueError:
    print("Ошибка: Введенное значение не является допустимым числом!")
