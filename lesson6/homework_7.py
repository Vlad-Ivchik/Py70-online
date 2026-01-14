# 7.	Дан список положительных целых чисел .
# # Вставить после каждого чётного числа его перевёртыш. 18 81, 42 24, 8 8, 122 221

lst = [24, 35, 48, 52, 64]
result = []

for i in lst:
    result.append(i)
    if i % 2 == 0:
        result_2 = int(str(i)[::-1])
        result.append(result_2)
print(result)

