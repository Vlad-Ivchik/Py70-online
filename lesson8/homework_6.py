# 6.	Сгенерировать список нечётных двузначных  чисел.


lst = []
for x in range(10, 100):
    if x % 2 == 1:
        lst.append(x)
print(lst)

