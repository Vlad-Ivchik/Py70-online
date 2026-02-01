# 1.	Создать класс с двумя переменными. Добавить функцию вывода на экран и функцию изменения этих переменных.
# Добавить функцию, которая находит сумму значений этих переменных, и функцию которая находит наибольшее значение из
# этих двух переменных

class Simple(object):

    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def set_number(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2
        return self

    def sum(self):
        return self.number_1 + self.number_2

    def max(self):
        return max(self.number_1, self.number_2)

    def __str__(self):
        return f"{self.number_1}, {self.number_2}"


simple_1 = Simple(10, 5)
print(simple_1)
simple_1.set_number(15, 10)
print(simple_1)
print(simple_1.max())
print(simple_1.sum())