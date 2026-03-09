SELECT
    m.movie_id,
    m.name_movie,
    m.release_year,
    m.budget,
    a.actor_id,
    a.name AS actor_name,
    a.surname AS actor_surname
FROM movies m
LEFT JOIN actors_movies am ON m.movie_id = am.movie_id
LEFT JOIN actors a ON am.actor_id = a.actor_id
WHERE m.budget > 150000000
ORDER BY m.budget DESC, m.name_movie, a.surname;