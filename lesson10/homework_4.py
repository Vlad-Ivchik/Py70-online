# 4.	Реализуйте класс MoneyBox, для работы с виртуальной копилкой. Каждая копилка имеет ограниченную вместимость,
# которая выражается целым числом – количеством монет(capacity -вместимость), которые можно положить в копилку.
# Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность добавлять монеты в копилку и узнавать,
# можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.


class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.bank = 0

    def can_add(self, v):
        return self.bank + v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.bank += v
            return True
        return False

    def show_bank(self):
        return self.bank


money_box1 = MoneyBox(30)
print(money_box1.can_add(5))
money_box1.add(5)
print(money_box1.show_bank())
print(money_box1.can_add(6))
print(money_box1.add(6))
print(money_box1.show_bank())
money_box1.add(5)
print(money_box1.show_bank())
money_box1.add(14)
print(money_box1.add(6))
print(money_box1.show_bank())
money_box1.add(14)
print(money_box1.show_bank())