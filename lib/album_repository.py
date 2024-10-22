from lib.album import Album

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

    # Read
    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row["title"], row["release_year"],row["artist_id"], row["id"])
            albums.append(item)
        return albums
    
    def single_album(self,album_id):
        rows = self._connection.execute('SELECT * from albums WHERE id = %s', [album_id])
        row = rows[0]
        return Album(row["title"], row["release_year"], row["artist_id"])

    # Create 
    def create(self, album):
        self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [
                        album.title, album.release_year, album.artist_id])
        return None