import pickle
import os


class Movies:
    def __init__(self, title, genre, director, year, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.title} - {self.genre}"


class MoviesModal:
    def __init__(self):
        self.db_name = 'movies.txt'
        self.movies = self.load_data()

    def add_movies(self, dict_movies):
        movies = Movies(*dict_movies.values())
        self.movies[movies.title] = movies

    def get_catalog_movies(self):
        return self.movies.values()

    def get_single_movie(self, movie_title):
        movie = self.movies[movie_title]
        dict_movies = {
            'название': movie.title,
            'жанр': movie.genre,
            'режиссер': movie.director,
            'год выпуска': movie.year,
            'длительность': movie.duration,
            'студия': movie.studio,
            'актеры': movie.actors
        }
        return dict_movies

    def del_single_movie(self, movie_title):
        title = self.movies.pop(movie_title)
        return title

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.db_name, 'wb') as f:
            pickle.dump(self.movies, f)
