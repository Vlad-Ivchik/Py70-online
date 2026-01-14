#3.	Дано число n. Посчитать сумму всех чётных чисел от 0 до n.

n = int(input())
count = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        count += i
print(count)


