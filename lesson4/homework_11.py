# 11.	Уберите точки из введенного IP-адреса. Выведите сначала четыре числа через пробел,
# а затем сумму получившихся чисел.
# Sample Input:
# 192.168.0.1
# Sample Output:
# 192 168 0 1
# 361

s = '192.168.0.1'
parts = s.split(".")

string = ''
summary = 0
for i in parts:
    string += i + ' '
    summary += int(i)
print(string)
print(summary)
