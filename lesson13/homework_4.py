# 4.	Имеется текстовый файл, содержащий 5 строк. Переписать каждую из его строк в список в том же порядке.


with open("text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

for i, line in enumerate(lines, 1):
    print(f"{i}: {line}")

