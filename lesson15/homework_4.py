SELECT 'Actor' AS role, a.actor_id AS id, a.name, a.surname, a.age, a.sex
FROM actors a
LEFT JOIN actors_movies am ON a.actor_id = am.actor_id
WHERE am.actor_id IS NULL
