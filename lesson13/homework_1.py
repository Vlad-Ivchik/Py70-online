# 1.	Создать текстовый файл и записать в него 6 строк. Записываемые строки вводятся с клавиатуры


with open("text.txt", "w", encoding="utf-8") as file:
    print("Введите 6 строк:")
    for i in range(6):
        line = input(f"Строка №{i + 1}: ")
        file.write(line + "\n")

print("Файл 'text.txt' создан")
