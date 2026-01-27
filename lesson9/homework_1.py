#1.	Написать декоратор log_result, который печатает результат выполнения функции.
# Применить к функции возведения числа в квадрат.


def log_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@log_result
def square(x):
    return x ** 2

square(5)

