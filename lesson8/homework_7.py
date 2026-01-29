# 7.	Сгенерировать список всех трёхзначных чисел кратных 5 и 3.

lst = []
for i in range(100, 1000):
    if i % 3 == 0 and i % 5 == 0:
        lst.append(i)
print(lst)