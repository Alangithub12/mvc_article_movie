from movie_model import Movie

class MovieController:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def remove_movie(self, movie):
        self.movies.remove(movie)

    def get_all_movies(self):
        return self.movies

    def find_movie_by_director(self, director):
        return [movie for movie in self.movies if movie.director == director]