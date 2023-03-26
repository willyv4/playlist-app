#Using the `movies_db` database, write the correct SQL queries for each of these tasks:

>

## 1. The title of every movie.

    SELECT title FROM movies;

---

>

## 2. All information on the G-rated movies.

    SELECT *
    FROM movies
    WHERE rating = 'G';

---

>

## 3. The title and release year of every movie, ordered with the oldest movie first.

    SELECT title, release_year
    FROM movies
    ORDER BY release_year;

---

>

## 4. All information on the 5 longest movies.

    SELECT \* FROM movies ORDER BY runtime DESC LIMIT 5;

---

>

## 5. A query that returns the columns of `rating` and `total`, tabulating the total number of G, PG, PG-13, and R-rated movies.

    SELECT rating, COUNT() as total
    FROM movies
    GROUP BY rating;

---

>

## 6. A table with columns of `release_year` and `average_runtime`, tabulating the average runtime by year for every movie in the database. The data should be in reverse chronological order (i.e. the most recent year should be first).

    SELECT release_year, AVG(runtime) AS average_runtime
    FROM movies
    GROUP BY release_year
    ORDER BY release_year DESC;

---

>

## 7. The movie title and studio name for every movie in the database.

    SELECT movies.title, studios.name
    FROM movies
    JOIN studios ON movies.studio_id = studios.id;

---

>

## 8. The star first name, star last name, and movie title for every matching movie and star pair in the database.

    SELECT stars.first_name, stars.last_name, movies.title
    FROM stars
    JOIN roles ON stars.id = roles.star_id
    JOIN movies ON movies.id = roles.movie_id;

---

>

## 9. The first and last names of every star who has been in a G-rated movie. The first and last name should appear only once for each star, even if they are in several G-rated movies. _IMPORTANT NOTE_: it's possible that there can be two _different_ actors with the same name, so make sure your solution accounts for that.

    SELECT stars.first_name, stars.last_name, movies.title
    FROM stars
    JOIN roles ON stars.id = roles.star_id
    JOIN movies ON movies.id = roles.movie_id;
    SELECT DISTINCT ON (stars.first_name, stars.last_name)
    stars.first_name, stars.last_name
    FROM stars
    JOIN roles ON stars.id = roles.star_id
    JOIN movies ON movies.id = roles.movie_id
    WHERE movies.rating = 'G'
    ORDER BY stars.first_name, stars.last_name;

---

>

## 10. The first and last names of every star along with the number of movies they have been in, in descending order by the number of movies. (Similar to #9, make sure that two different actors with the same name are considered separately).

    SELECT stars.first_name, stars.last_name, COUNT(DISTINCT roles.movie_id) AS num_movies
    FROM stars
    JOIN roles ON stars.id = roles.star_id
    JOIN movies ON roles.movie_id = movies.id
    WHERE movies.rating = 'G'
    GROUP BY stars.id
    ORDER BY num_movies DESC;
