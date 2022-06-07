from db.run_sql import run_sql

from models.album import Album
import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (album_name, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.album_name, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist_id = result["artist_id"]
        artist = artist_repository.select(artist_id)
        album = Album(
            result['album_name'],
            result['genre'],
            artist,
            result['id']
            )
    return album

def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist_id = row["artist_id"]
        artist = artist_repository.select(artist_id)
        album = Album(row['album_name'], row['genre'], artist, row['id'] )
        albums.append(album)
    return albums 


