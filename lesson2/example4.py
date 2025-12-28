# Написать программу с вызовом type два раза соответственно для двух переменных разных типов. Результаты на экран
# А потом вызвать для них же isinstance. Результаты вывести на экран
from operator import is_none

test_int = 6
print(test_int)
test_str = "hello"
print(test_str)

print(isinstance(test_int, int))
print(isinstance(test_str, str))
