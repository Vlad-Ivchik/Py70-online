# 13.	Посчитать средний возраст мужчин и женщин.

SELECT
    sex,
    ROUND(AVG(age), 1) AS average_age
FROM actors
WHERE age IS NOT NULL
GROUP BY sex;