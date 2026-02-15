#11.	Посчитать и вывести общее количество актёров, средний возраст, минимальный и максимальный возраст

SELECT
    COUNT(*) AS total_actors,
    AVG(age) AS average_age,
    MIN(age) AS min_age,
    MAX(age) AS max_age
FROM actors;