# 9.	Вывести актрис из Франции младше 35 лет.

SELECT id, name, last_name, age, sex, country
FROM actors
WHERE sex = 'female'
  AND country = 'France'
  AND age < 35;