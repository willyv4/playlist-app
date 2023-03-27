from app import db
from models import Playlist, Song, PlaylistSong
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text


# Create all tables
db.drop_all()
db.create_all()

# Create playlists
rock = Playlist(name='Rock', description='Awesome rock songs')
pop = Playlist(name='Pop', description='Popular pop songs')
indie = Playlist(name="Indie", description="My favorite kind of music")
jazz = Playlist(name="Jazz", description="Music that doesn't make sense")

db.session.add(rock)
db.session.add(pop)
db.session.add(indie)
db.session.add(jazz)
db.session.commit()

# Create songs

song1 = Song(title='Stairway to Heaven', artist='Led Zeppelin')
song2 = Song(title='Bohemian Rhapsody', artist='Queen')
song3 = Song(title='Thriller', artist='Michael Jackson')
song4 = Song(title='Billie Jean', artist='Michael Jackson')
song5 = Song(title='Kids', artist='MGMT')
song6 = Song(title='Sleepyhead', artist='Passion Pit')
song7 = Song(title='Take Five', artist='Dave Brubeck Quartet')
song8 = Song(title='So What', artist='Miles Davis')


db.session.add(song1)
db.session.add(song2)
db.session.add(song3)
db.session.add(song4)
db.session.add(song5)
db.session.add(song6)
db.session.add(song7)
db.session.add(song8)
db.session.commit()

# Add songs to playlists
pl1 = PlaylistSong(playlist_id=rock.id, song_id=song1.id)
pl2 = PlaylistSong(playlist_id=rock.id, song_id=song2.id)

pl3 = PlaylistSong(playlist_id=indie.id, song_id=song5.id)
pl4 = PlaylistSong(playlist_id=indie.id, song_id=song6.id)

pl5 = PlaylistSong(playlist_id=jazz.id, song_id=song7.id)
pl6 = PlaylistSong(playlist_id=jazz.id, song_id=song8.id)


# Add playlists and songs to the session
db.session.add(pl1)
db.session.add(pl2)
db.session.add(pl3)
db.session.add(pl4)
db.session.add(pl5)
db.session.add(pl6)
# Commit the changes
db.session.commit()
