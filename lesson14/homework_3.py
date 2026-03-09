# 3.	Добавьте проверку, что age не может быть меньше 0.


ALTER TABLE actors
ADD CONSTRAINT age_positive CHECK (age >= 0);