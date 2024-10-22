from lib.album_repository import AlbumRepository
from lib.album import Album


def test_get_all_albums(db_connection): 
    db_connection.seed("seeds/music_tables.sql") 
    repository = AlbumRepository(db_connection) 

    albums = repository.all() 

    assert albums == [
        Album('Vulgar display of power', 1992, 2, 1),
        Album('Cowboys from hell', 1990, 2, 2),
        Album('Follow the leader', 1998, 1, 3),
        Album('Untouchables', 2002, 1, 4),
        Album('Bloody kisses', 1993, 3, 5)
    ]

def test_get_single_album(db_connection): 
    db_connection.seed("seeds/music_tables.sql") 
    repository = AlbumRepository(db_connection) 

    album = repository.single_album(1) 

    assert album == Album('Vulgar display of power', 1992, 2)

def test_create_album(db_connection):
    db_connection.seed("seeds/music_tables.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album("Korn", 1994, 1))

    result = repository.all()
    assert result == [
        Album('Vulgar display of power', 1992, 2, 1),
        Album('Cowboys from hell', 1990, 2, 2),
        Album('Follow the leader', 1998, 1, 3),
        Album('Untouchables', 2002, 1, 4),
        Album('Bloody kisses', 1993, 3, 5),
        Album("Korn", 1994, 1,6)
    ]

