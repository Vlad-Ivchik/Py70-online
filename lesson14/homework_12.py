# 12.	Вывести страны, в которых более 5 и менее 10 актёров.

SELECT country, COUNT(*) AS actor_count
FROM actors
GROUP BY country
HAVING COUNT(*) > 5 AND COUNT(*) < 10
ORDER BY actor_count DESC;