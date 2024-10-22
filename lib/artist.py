class Artist:
    def __init__(self, name, genre, id=None):
        self.name = name
        self.genre = genre
        self.id = id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Artist(Name:{self.name}, Genre:{self.genre})"