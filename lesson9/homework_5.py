# 5.	Дан список: ['apple', 'Banana', 'cherry', 'DATE'].
# Получите новый список, оставив только слова в нижнем регистре

words = ['apple', 'Banana', 'cherry', 'DATE']

lower_words = [word for word in words if word.islower()]

print(lower_words)
