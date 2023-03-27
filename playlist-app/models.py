"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()


class Playlist(db.Model):
    __tablename__ = "playlists"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    songs = db.relationship(
        "Song", secondary="playlists_songs", backref="songs_in_playlist")


class Song(db.Model):
    __tablename__ = "songs"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    artist = db.Column(db.Text, nullable=False)
    playlists = db.relationship(
        "Playlist", secondary="playlists_songs", backref="playlist_with_song")


class PlaylistSong(db.Model):
    __tablename__ = "playlists_songs"
    id = db.Column(db.Integer, primary_key=True)
    
    playlist_id = db.Column(db.Integer, db.ForeignKey(
        "playlists.id"), nullable=False)

    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"), nullable=False)

    playlists = db.relationship(
        'Playlist', backref=db.backref("playlists_songs"))
    songs = db.relationship('Song', backref=db.backref("playlists_songs"))


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
