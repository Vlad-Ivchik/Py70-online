#1. Создайте класс RangeIterator, который реализует протокол итератора (__iter__, __next__).
# Итератор должен возвращать числа в заданном диапазоне с указанным шагом.
# После окончания итерации должно выбрасываться исключение StopIteration

class RangeIterator:
    def __init__(self, start, end, step=1):
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0 and self.current >= self.end:
            raise StopIteration
        if self.step < 0 and self.current <= self.end:
            raise StopIteration
        result = self.current
        self.current += self.step
        return result

for num in RangeIterator(0, 10, 2):
    print(num)
