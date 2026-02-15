# 5.	Имеется текстовый файл. Получить текст, в котором в конце каждой строки из заданного файла добавлен восклицательный знак


with open("text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

edit_lines = [line.rstrip("\n") + "!\n" for line in lines]

with open("text.txt", "w", encoding="utf-8") as file:
    file.writelines(edit_lines)

print(f"Файл успешно обработан. Результат сохранен в {"text.txt"}")
