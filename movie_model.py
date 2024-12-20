class Movie:
    def __init__(self, title, genre, director, year, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors  # Список кортежей (ФИО, роль)

    def __str__(self):
        actors_str = ", ".join([f"{actor[0]} как {actor[1]}" for actor in self.actors])
        return f"Фильм: {self.title} | Жанр: {self.genre} | Режиссер: {self.director} | Год: {self.year} | Длительность: {self.duration} мин | Студия: {self.studio} | Актеры: {actors_str}"