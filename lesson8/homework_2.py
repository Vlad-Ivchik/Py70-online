# 2.	Дано натуральное число n > 1. Проверьте, является ли оно совершенным.
# Программа должна вывести слово YES, если число совершенное и NO, в противном случае.

def perfect_number(n):
    n = int(input())
    summ = 0

    for i in range(1, n):
        if n % i == 0:
            summ += i

    if summ == n:
        print("YES")
    else:
        print("NO")


perfect_number(5)
