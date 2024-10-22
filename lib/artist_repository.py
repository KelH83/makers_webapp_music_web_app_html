from lib.artist import Artist

class ArtistRepository:
    def __init__(self, connection):
        self._connection = connection

    # Read
    def all(self):
        rows = self._connection.execute('SELECT * from artists')
        artists = []
        for row in rows:
            item = Artist(row["name"], row["genre"])
            artists.append(item)
        return artists
    
    def single_artist(self,artist_id):
        rows = self._connection.execute('SELECT * from artists WHERE id = %s', [artist_id])
        row = rows[0]
        return Artist(row["name"], row["genre"])


    # Create 
    def create(self, artist):
        self._connection.execute('INSERT INTO artists (name,genre) VALUES (%s, %s)', [
                        artist.name,artist.genre])
        return None