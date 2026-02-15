# 8.	Повысить возраст на 2 года всем актрисам (female) старше 40 лет.

UPDATE actors
SET age = age + 2
WHERE sex = 'female' AND age > 40;