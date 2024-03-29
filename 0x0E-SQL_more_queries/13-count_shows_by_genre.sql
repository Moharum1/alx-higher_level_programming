-- a Script that shows how many time a genres appeared in a movie
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows 
FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;