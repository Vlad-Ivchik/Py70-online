# 3.	Написать декоратор bench, который измеряет ошибки: если функция завершилась ошибкой, вывести её тип и сообщение.


def bench(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            print(f"Все правильно работает!")
            return result
        except Exception as e:
            print(f"Ошибка в функции {func.__name__}")
            print(f"Тип ошибки: {type(e).__name__}")
            print(f"Сообщение: {e}")


    return wrapper


@bench
def function(x):
    return 2 / x


function(0)
