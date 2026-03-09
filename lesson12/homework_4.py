def flatten(iterable):
    for item in iterable:
        if isinstance(item, (list, tuple)) and not isinstance(item, (str, bytes)):
            yield from flatten(item)
        else:
            yield item

nested_list = [1, [2, 3, [4, 5]], 6, [7, 8], 9]
flat_list = list(flatten(nested_list))
print(f"Исходный список: {nested_list}")
print(f"Плоский список: {flat_list}") 

mixed = [[1, 2], [[[3]]], 4]
print(list(flatten(mixed))) 

