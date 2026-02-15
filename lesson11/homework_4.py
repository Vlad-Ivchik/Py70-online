# 4.	Создай класс BankAccount, который имеет закрытый баланс __balance. Позволяет пополнять deposit и снимать withdraw деньги.
# Не позволяет снимать больше, чем есть на счету. Вводит суточный лимит снятия (например, 5000).
# Сделайте ограничение по транзакциям, не более 3 – х

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Добавлено {amount} на баланс")
        else:
            print("Депозит должен быть положительным")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств на балансе")
        else:
            self.balance -= amount
            print(f"Было снято {amount} с баланса")


# Пример использования:
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)
