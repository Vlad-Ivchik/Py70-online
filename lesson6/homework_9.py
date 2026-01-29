#9.	 *Дан список . Перезаписать его так, чтобы сначала были все положительные числа, а затем все отрицательные и нули,
# сохраняя порядок их следования. [5,2,0,-2,-7,1,8,0,-1] -> [5,2,1,8,-2,-7,-1,0,0]

original_list = [5, 2, 0, -2, -7, 1, 8, 0, -1]
positive_numbers = []
non_positive_numbers = []
nol = []

for num in original_list:
    if num > 0:
        positive_numbers.append(num)
    elif num == 0:
        nol.append(num)
    else:
        non_positive_numbers.append(num)

result_list = positive_numbers + non_positive_numbers + nol
print(result_list)

