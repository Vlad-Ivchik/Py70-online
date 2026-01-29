#4.	Дан список. Пользователь не знает его размер.
# Программа должна бросить исключение TypeError, когда пользователь пытается удалить элемент которого нет в списке.

lst = [5, 7, 9]
remove_number = 7

try:
    lst.remove(remove_number)
except ValueError:
    print(f"Элемент '{remove_number}' не найден в списке.")

print(lst)
