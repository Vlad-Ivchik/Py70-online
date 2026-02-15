# 3.	Дан текстовый файл. Подсчитать количество символов в нем. Без \n


with open("text.txt", "r", encoding="utf-8") as file:
    data = file.read()
    # Удаляем все символы переноса строки
    without_n = data.replace("\n", "")
    count = len(without_n)
    print(f"Количество символов в файле {"text.txt"} (без \\n): {count}")