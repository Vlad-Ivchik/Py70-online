# 14.	Для каждой страны вывести самого молодого актёра.

SELECT
    country,
    name,
    last_name,
    age,
    sex
FROM actors
WHERE (country, age) IN (
    SELECT country, MIN(age)
    FROM actors
    WHERE age IS NOT NULL
    GROUP BY country
)
ORDER BY country;