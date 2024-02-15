-- a Script that shows how many time a genres appeared in a movie
SELECT name
FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter"
ORDER BY name;