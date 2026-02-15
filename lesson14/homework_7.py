# 7.	Установите страну "Unknown" всем актёрам, у которых она NULL.

UPDATE actors
SET country = 'Unknown'
WHERE country IS NULL;