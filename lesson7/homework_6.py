# 6.	Дана строка, содержащая числа, разделённые пробелами.
# Нужно вывести их сумму. Если хотя бы один элемент не является числом — перехватить исключение и пропустить его.
# "10 5 abc 3" → 18

string = "10 5 abc 3"
summary = 0
elements = string.split()

for i in elements:
    try:
        number = int(i)
        summary += number
    except ValueError:
        print(f"Элемент не является числом: '{i}'")
print(f"Сумма элементов: {summary}")
