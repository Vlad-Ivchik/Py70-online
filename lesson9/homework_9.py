# 9.	Дан список кортежей (товар, цена, количество).
# Получить список сумм: цена * количество.


items = [('Шины', 50, 10), ('Диски', 30, 5), ('Колодки', 40, 8)]

lst_sums = [price * quantity for i, price, quantity in items]

print(lst_sums)
