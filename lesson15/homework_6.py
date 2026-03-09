SELECT DISTINCT d.director_id, d.name, d.surname, d.age, d.sex
FROM directors d
JOIN movies m ON d.director_id = m.director_id
WHERE m.release_year < 2000
  AND m.director_id IS NOT NULL
ORDER BY d.surname, d.name;