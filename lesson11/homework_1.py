# 1.	Создайте абстрактный класс PaymentMethod. Объявить абстрактный метод pay(amount).
# Реализовать минимум 3 класса-наследника с разной логикой оплаты. Обеспечить возможность работать с объектами через общий интерфейс.
# Проверить полиморфное поведение при вызове pay

from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class ApplePay(PaymentMethod):
    def pay(self, amount):
        print(f'Оплачено черещ ApplePay: {amount} $')

class SamsungPay(PaymentMethod):
    def pay(self, amount):
        print(f'Оплачено черещ SamsungPay: {amount} $')

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f'Оплачено черещ PayPal: {amount} $')


pay_method_1 = ApplePay()
pay_method_2 = SamsungPay()
pay_method_3 = PayPal()

pay_method_1.pay(10)
pay_method_2.pay(50)
pay_method_3.pay(100)