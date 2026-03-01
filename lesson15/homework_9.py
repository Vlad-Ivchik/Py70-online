WITH avg_rating_before_2000 AS (
    SELECT AVG(rating) as avg_rating
    FROM movies
    WHERE release_year < 2000 AND rating IS NOT NULL
)

SELECT
    d.director_id,
    d.name AS director_name,
    d.surname AS director_surname,
    m.movie_id,
    m.name_movie,
    m.release_year,
    m.rating,
    ROUND((SELECT avg_rating FROM avg_rating_before_2000), 2) AS avg_rating_all
FROM directors d
JOIN movies m ON d.director_id = m.director_id
WHERE m.release_year < 2000
  AND m.rating IS NOT NULL
  AND m.rating < (SELECT avg_rating FROM avg_rating_before_2000)
ORDER BY m.rating ASC;