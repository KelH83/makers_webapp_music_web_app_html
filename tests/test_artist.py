from lib.artist import Artist
"""
artist constructs with an id, artist id, title and release year
"""
def test_Artist_constructs():
    artist = Artist("Slayer", "Metal")
    assert artist.name == "Slayer"
    assert artist.genre == "Metal"

"""
We can format Artists to strings nicely
"""
def test_Artist_format_nicely():
    artist = Artist("Slayer", "Metal")
    assert str(artist) == "Artist(Name:Slayer, Genre:Metal)"