ALTER TABLE movies
ADD COLUMN rating DECIMAL(3,1) NULL;


UPDATE movies SET rating = 7.9 WHERE movie_id = 1;
UPDATE movies SET rating = 8.1 WHERE movie_id = 2;
UPDATE movies SET rating = 8.8 WHERE movie_id = 3;
UPDATE movies SET rating = 8.5 WHERE movie_id = 4;
UPDATE movies SET rating = 7.6 WHERE movie_id = 5;
UPDATE movies SET rating = 8.2 WHERE movie_id = 6;
UPDATE movies SET rating = 7.2 WHERE movie_id = 7;
UPDATE movies SET rating = 6.1 WHERE movie_id = 8;
UPDATE movies SET rating = 7.7 WHERE movie_id = 9;
UPDATE movies SET rating = 7.3 WHERE movie_id = 10;
UPDATE movies SET rating = 6.8 WHERE movie_id = 11;
UPDATE movies SET rating = 7.1 WHERE movie_id = 12;
UPDATE movies SET rating = 7.8 WHERE movie_id = 13;
UPDATE movies SET rating = 6.6 WHERE movie_id = 14;
UPDATE movies SET rating = 6.9 WHERE movie_id = 15;
UPDATE movies SET rating = 6.7 WHERE movie_id = 16;
UPDATE movies SET rating = 7.6 WHERE movie_id = 17;
UPDATE movies SET rating = 8.0 WHERE movie_id = 18;
UPDATE movies SET rating = 8.6 WHERE movie_id = 19;
