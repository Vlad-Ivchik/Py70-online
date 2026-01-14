#4.	Дано натуральное число. Определить произведение цифр в нем которые кратны 2, кроме числа 0.

x = int(input())
count = 1
for i in range(1, x + 1):
    if i % 2 == 0 and i != 0:
        count *= i
print(count)
