#8.	Дан список ['cat','car','mouse','dog','snake','cow'].
#Получить словарь: {начальная буква: [слова...]}.

words = ['cat', 'car', 'mouse', 'dog', 'snake', 'cow']

first_letters = set(word[0] for word in words)


result = {
    letter: [word for word in words if word[0] == letter]
    for letter in first_letters
}

print(result)