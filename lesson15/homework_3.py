SELECT DISTINCT d.director_id, d.name, d.surname, d.age, d.sex
FROM directors d
JOIN movies m ON d.director_id = m.director_id
WHERE m.director_id IS NOT NULL
ORDER BY m.budget DESC
LIMIT 10;