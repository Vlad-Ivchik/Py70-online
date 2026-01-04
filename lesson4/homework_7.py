# 7.	Дано слово. Верно ли, что оно начинается и оканчивается на одну и ту же букву?

string = input()

string_1 = string.lower()[0]
string_2 = string.lower()[-1]

if string_1 == string_2:
    print(True)
else:
    print(False)
