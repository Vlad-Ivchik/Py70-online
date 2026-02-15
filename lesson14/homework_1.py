# 1.	Создайте таблицу actors со следующими полями:
# •	id — INTEGER PRIMARY KEY AUTOINCREMENT
# •	age — INTEGER
# •	sex — TEXT, допускаются только значения 'male' и 'female'
# •	country — TEXT
# •	name — TEXT NOT NULL
# •	last_name — TEXT NOT NULL

CREATE TABLE actors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age INTEGER,
    sex TEXT CHECK(sex IN ('male', 'female')),
    country TEXT,
    name TEXT NOT NULL,
    last_name TEXT NOT NULL
);
