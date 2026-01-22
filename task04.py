class Movie:
    def __init__(self, title, genre, duration, rating):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating

    def info(self):
        return f"Movie(title='{self.title}', genre='{self.genre}', duration='{self.duration}', rating='{self.rating}')"

title = input('Title: ')
genre = input('Genre: ')
duration = int(input('Duration: '))
rating = float(input('Rating: '))

movie = Movie(title, genre, duration, rating)

print(movie.info())