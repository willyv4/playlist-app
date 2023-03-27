from curses import flash
from turtle import title
from flask import Flask, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from config import secret_key
from forms import SongForm, PlaylistForm, NewSongForPlaylistForm
from models import db, connect_db, Playlist, Song, PlaylistSong


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = secret_key
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route("/")
def root():
    """Homepage: redirect to /playlists."""
    return redirect("/playlists")


##############################################################################
# Playlist routes


@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""
    # Get the playlist with the given ID or return a 404 error if not found
    playlist = Playlist.query.filter_by(id=playlist_id).first_or_404()

    # Join the Song table with the PlaylistSong table and filter by
    # the playlist_id to get all songs in the playlist
    songs = Song.query.join(PlaylistSong).filter(
        PlaylistSong.playlist_id == playlist_id).all()

    return render_template("playlist.html", songs=songs, playlist=playlist)


@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """
    form = PlaylistForm()

    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data

        playlist = Playlist(name=name, description=description)
        db.session.add(playlist)
        db.session.commit()
        flash("Playlist added succesfully")
        return redirect('/playlists')
    return render_template("new_playlist.html", form=form)
    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK


##############################################################################
# Song routes


@app.route("/songs")
def show_all_songs():
    """Show list of songs."""

    songs = Song.query.all()
    return render_template("songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""

    # Get the song with the given ID or return a 404 error if not found
    song = Song.query.filter_by(id=song_id).first_or_404()

    # Join the Playlist table with the PlaylistSong table and filter by
    # the song_id to get all playlists associated with song
    playlists = Playlist.query.join(PlaylistSong).filter(
        PlaylistSong.song_id == song_id).all()

    return render_template("song.html", playlists=playlists, song=song)


@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """
    form = SongForm()

    if form.validate_on_submit():
        title = form.title.data
        artist = form.artist.data
        song = Song(title=title, artist=artist)
        db.session.add(song)
        db.session.commit()
        flash("Song added succesfully")
        return redirect("/songs")
    return render_template("new_song.html", form=form)

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK


@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""

    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()

    # query songs currently on playlist
    curr_on_playlist = [song.id for song in playlist.songs]
    # retreive all songs and filter out songs currently on playlist
    form.song.choices = (db.session.query(Song.id, Song.title)
                         .filter(Song.id.notin_(curr_on_playlist))
                         .all())

    if form.validate_on_submit():
        playlist_song = PlaylistSong(
            song_id=form.song.data, playlist_id=playlist_id)

        db.session.add(playlist_song)
        db.session.commit()

        return redirect(f"/playlists/{playlist_id}")

    return render_template("add_song_to_playlist.html",
                           playlist=playlist,
                           form=form)
