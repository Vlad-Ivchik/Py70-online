# 8.	Проверить является ли строка палиндромом.

string = input()

string_1 = string.lower()
string_2 = string.lower()[::-1]

if string_1 == string_2:
    print("Строка палиндром")
else:
    print("Строка не палиндром")
