# 2.	Описать класс, реализующий десятичный счетчик, который может увеличивать или уменьшать свое значение на единицу
# в заданном диапазоне. Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.
# Счетчик имеет два метода: увеличения и уменьшения, — и свойство, позволяющее получить его текущее состояние.
# Написать программу, демонстрирующую все возможности класса.

class Counter:
    def __init__(self, min_value, max_value, start_value=None):
        self.min_val = min_value
        self.max_val = max_value
        self.value = start_value

    def increase(self):
        if self.value < self.max_val:
            self.value += 1
        else:
            print("Достигнут максимум")

    def decrease(self):
        if self.value > self.min_val:
            self.value -= 1
        else:
            print("Достигнут минимум")

    def get_value(self):
        return self.value

# Пример использования
counter = Counter(min_value=0, max_value=10, start_value=5)
counter.increase() # 6
print(counter.get_value())
counter.increase() # 6
print(counter.get_value())
counter.increase() # 6
print(counter.get_value())
counter.increase() # 6
print(counter.get_value())
counter.increase() # 6
print(counter.get_value())
counter.increase() # 6
print(counter.get_value())
counter.increase() # 6
print(counter.get_value())
counter.decrease() # 5
print(counter.get_value())
counter.decrease() # 5
print(counter.get_value())
counter.decrease() # 5
print(counter.get_value())
counter.decrease() # 5
print(counter.get_value())
counter.decrease() # 5
print(counter.get_value())
counter.decrease() # 5
print(counter.get_value())
counter.decrease() # 5
print(counter.get_value())
counter.decrease() # 5
print(counter.get_value())
counter.decrease() # 5
print(counter.get_value())
counter.decrease() # 5
print(counter.get_value())
counter.decrease() # 5
print(counter.get_value())
counter.decrease() # 5
print(counter.get_value())