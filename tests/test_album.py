from lib.album import Album
"""
album constructs with an id, artist id, title and release year
"""
def test_album_constructs():
    album = Album("Test Title", 1999, 2, 1)
    assert album.artist_id == 2
    assert album.title == "Test Title"
    assert album.release_year == 1999
    assert album.id == 1

"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    album = Album("Test Title", 1999, 2,1)
    assert str(album) == "Album(Title:Test Title, Release year:1999, Artist ID:2)"