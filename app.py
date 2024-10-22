import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist import Artist
from lib.artist_repository import ArtistRepository

app = Flask(__name__)

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app) 
    repository = AlbumRepository(connection)
    all_albums = repository.all()
    return_list = []
    for album in all_albums:
        return_list.append(album)
    return render_template('albums.html',return_list=return_list)

@app.route('/albums/<int:album_id>', methods=['GET'])
def get_single_album(album_id):
    connection = get_flask_database_connection(app) 
    repository = AlbumRepository(connection)
    single_album = repository.single_album(album_id)
    artist_repository = ArtistRepository(connection)
    single_artist = artist_repository.single_artist(single_album.artist_id)

    return render_template('single_album.html',single_album=single_album, single_artist=single_artist)



@app.route('/albums/new', methods=['GET'])
def get_new_album():
            return render_template('album_new.html')

@app.route('/albums', methods=['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    artist_repository = ArtistRepository(connection)

    title = request.form['title']
    release_year = request.form['release_year']
    artist_name = request.form['artist_name']
    artist = artist_repository.search_by_name(artist_name)

    album = Album(title, release_year, artist.id)

    if not album.is_valid():
        return render_template('albums/new.html', album=album, errors=album.generate_errors()), 400

    album = repository.create(album)

    return redirect(f"/albums/{album.id}")

@app.route('/artists/new', methods=['GET'])
def get_new_artist():
            return render_template('artist_new.html')

@app.route('/artists', methods=['POST'])
def create_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    name = request.form['name']
    genre = request.form['genre']

    artist = Artist(name, genre)

    if not artist.is_valid():
        return render_template('artists/new.html', artist=artist, errors=artist.generate_errors()), 400

    artist = repository.create(artist)

    return redirect(f"/artists/{artist.id}")


@app.route('/artists', methods=['POST'])
def post_artist():
    connection = get_flask_database_connection(app) 
    name = request.form['name']
    genre = request.form['genre']
    repository = ArtistRepository(connection)

    repository.create(Artist(name, genre))

    return 'Created'

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app) 
    repository = ArtistRepository(connection)
    all_artists = repository.all()
    return_list = []
    for artist in all_artists:
        return_list.append(artist)
    return render_template('artists.html',return_list=return_list)

@app.route('/artists/<int:artist_id>', methods=['GET'])
def get_single_artist(artist_id):
    connection = get_flask_database_connection(app) 
    repository = ArtistRepository(connection)
    single_artist = repository.single_artist(artist_id)

    return render_template('single_artist.html', single_artist=single_artist)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
