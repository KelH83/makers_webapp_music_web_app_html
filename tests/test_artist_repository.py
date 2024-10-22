from lib.artist_repository import ArtistRepository
from lib.artist import Artist


def test_get_all_artists(db_connection): 
    db_connection.seed("seeds/music_tables.sql") 
    repository = ArtistRepository(db_connection) 

    artists = repository.all() 

    assert artists == [
        Artist('Korn', 'Metal'),
        Artist('Pantera', 'Metal'),
        Artist('Type O Negative', 'Metal'),
        Artist('Pentatonix', 'Pop')
    ]

def test_get_single_artist(db_connection): 
    db_connection.seed("seeds/music_tables.sql") 
    repository = ArtistRepository(db_connection) 

    artist = repository.single_artist(1) 

    assert artist == Artist('Korn', 'Metal')


def test_create_artist(db_connection):
    db_connection.seed("seeds/music_tables.sql")
    repository = ArtistRepository(db_connection)

    repository.create(Artist("Slayer", "Metal"))

    result = repository.all()
    assert result == [
        Artist('Korn', 'Metal'),
        Artist('Pantera', 'Metal'),
        Artist('Type O Negative', 'Metal'),
        Artist('Pentatonix', 'Pop'),
        Artist('Slayer', 'Metal')
    ]