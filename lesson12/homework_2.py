# 2. Напишите генераторную функцию fibonacci(limit),которая возвращает последовательность Фибоначчи до заданного предела.
# Генерация должна останавливаться, когда значение превышает limit

def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


for num in fibonacci(111):
    print(num)

