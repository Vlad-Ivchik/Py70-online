#2.	Создайте абстрактный класс Notification. Объявите абстрактный метод send(message).
# Реализуйте минимум 3 класса-наследника, каждый из которых отправляет сообщение по-разному
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print(f"Email notification: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"Sms notification: {message}")

class TelegramNotification(Notification):
    def send(self, message):
        print(f"Telegram notification: {message}")


notification_1 = EmailNotification()
notification_2 = SMSNotification()
notification_3 = TelegramNotification()

notification_1.send("Hello")
notification_2.send("Bye bye")
notification_3.send("Come on")