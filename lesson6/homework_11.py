# 11.	Во входной строке записана последовательность чисел через пробел.
# Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO,
# если не встречалось.

input_string = input()
numbers_str = input_string.split()
seen_numbers = set()

for i in numbers_str:
    if i in seen_numbers:
        print("YES")
    else:
        print("NO")
        seen_numbers.add(i)

