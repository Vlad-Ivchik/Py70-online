# 2.	Написать декоратор repeat(n), который повторяет вызов функции n раз и возвращает последний результат.


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = 0
            for i in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(5)
def addition(x, y):
    print(f"Сложение {x} + {y}")
    return x + y


print(f'Последний результат: {addition(3, 4)}')
