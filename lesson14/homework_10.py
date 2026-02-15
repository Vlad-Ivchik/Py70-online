# Вывести 5 самых молодых актёров.


SELECT id, name, last_name, age, sex, country
FROM actors
WHERE age IS NOT NULL
ORDER BY age ASC
LIMIT 5;