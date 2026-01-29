# 9.	Напишите программу, на вход которой подаётся список чисел одной строкой.
# Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
# Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка.
# Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
# Если на вход пришло только одно число, надо вывести его же.
# Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом

def prog():

    numbers = list(map(int, input().split()))

    if len(numbers) == 1:
        print(numbers[0])
        return

    result = []
    len_numbers = len(numbers)

    for i in range(len_numbers):

        left_number = (i - 1) % len_numbers
        right_number = (i + 1) % len_numbers
        summ = numbers[left_number] + numbers[right_number]
        result.append(summ)

    print(' '.join(map(str, result)))

prog()