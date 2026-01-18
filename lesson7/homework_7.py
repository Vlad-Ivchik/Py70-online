# 7.	Написать алгоритм, считающий частоту букв в строке.
# Если входные данные — не строка, выбросить TypeError.

string = "aaa bb ss rra aa b"

if not isinstance(string, str):
    raise TypeError(f"Входные данные не строка, а {type(string)}")

frequency = {}

for i in string:
    if i.isalpha():
        i_lower = i.lower()
        frequency[i_lower] = frequency.get(i_lower, 0) + 1

print(frequency)
