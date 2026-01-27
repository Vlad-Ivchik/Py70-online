# 7.	Дан список списков: [[1,2],[3,4],[5,6]]. С помощью reduce объединить в один список: [1,2,3,4,5,6].

from functools import reduce

lst = [[1, 2], [3, 4], [5, 6]]

result = reduce(lambda x, y: x + y, lst)

print(result)
