-- a Script that list all the movies with at least one genres from the geners db
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
    JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    ORDER BY tv_shows.title , tv_show_genres.genre_id;