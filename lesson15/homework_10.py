WITH actor_collaborations AS (
    SELECT DISTINCT
        am1.actor_id AS actor1,
        am2.actor_id AS actor2
    FROM actors_movies am1
    JOIN actors_movies am2 ON am1.movie_id = am2.movie_id
    WHERE am1.actor_id != am2.actor_id  -- Исключаем самого себя
      AND am1.actor_id IS NOT NULL
      AND am2.actor_id IS NOT NULL
),
actor_collaboration_counts AS (
    SELECT
        actor1 AS actor_id,
        COUNT(DISTINCT actor2) AS co_actors_count
    FROM actor_collaborations
    GROUP BY actor1
)
SELECT
    a.actor_id,
    a.name,
    a.surname,
    a.age,
    a.sex,
    acc.co_actors_count
FROM actors a
JOIN actor_collaboration_counts acc ON a.actor_id = acc.actor_id
WHERE acc.co_actors_count >= 2
ORDER BY acc.co_actors_count DESC, a.surname, a.name;