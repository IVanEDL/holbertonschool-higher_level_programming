-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres
INNER JOIN tv_shows
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;