# 6.	Дано число n. Вывести на экран числа 1, 4, 9, 16, 25, ... которые меньше n.
# Sample Input :
# 15
# Sample Output :
# 1 4 9


n = int(input())

for i in range(1, n + 1):
    if i ** 2 <= n:
        print(i ** 2, end=' ')
