"""Forms for playlist app."""

from wtforms import SelectField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, URL, Optional, NumberRange, AnyOf


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    # Add the necessary code to use this form
    name = StringField("Name", validators=[InputRequired(
        message="Please enter a playlist name.")])
    description = StringField(
        "Description", validators=[InputRequired(message="Please enter a description.")])


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField("Title", validators=[InputRequired(
        message="Please enter a song title.")])
    artist = StringField(
        "Artist", validators=[InputRequired(message="Please enter an artist.")])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int, validators=[
                       InputRequired(message="Please select a song.")])
