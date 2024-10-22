import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist import Artist
from lib.artist_repository import ArtistRepository


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/emoji', methods=['GET'])
def get_emoji():
    return render_template('emoji.html', emoji=':)')

@app.route('/goodbye', methods=['GET'])
def get_goobye():
    return render_template('goodbye.html')

@app.route('/greet')
def greet():
    name = request.args.get('name')
    return render_template('greet.html', name=name)

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


@app.route('/albums', methods=['POST'])
def post_album():
    connection = get_flask_database_connection(app) 
    title = request.form['title']
    release_year = request.form['release_year']
    artist = request.form['artist_id']
    repository = AlbumRepository(connection)

    repository.create(Album(title, release_year, artist))

    return 'Created'

@app.route('/artists', methods=['GET'])
def get_artist():
    connection = get_flask_database_connection(app) 
    repository = ArtistRepository(connection)
    all_artists = repository.all()
    return_list = []
    for artist in all_artists:
        return_list.append(str(artist))
    return return_list

@app.route('/artists', methods=['POST'])
def post_artist():
    connection = get_flask_database_connection(app) 
    name = request.form['name']
    genre = request.form['genre']
    repository = ArtistRepository(connection)

    repository.create(Artist(name, genre))

    return 'Created'


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
