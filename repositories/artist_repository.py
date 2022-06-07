from db.run_sql import run_sql
from models.artist import Artist

def save(artist):
  sql = "INSERT INTO artists (artist_title) VALUES (%s) RETURNING *"
  values = [artist.artist_title]
  result = run_sql(sql, values)
  id = result[0]['id']
  artist.id = id
  return artist

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def select(id):
  artist = None
  sql = "SELECT * FROM artists WHERE id = %s"
  values = [id]
  result = run_sql(sql, values)[0]
  if result is not None:
    artist = Artist(result["artist_title"], result["id"])
  return artist

def select_all():
  artists = []
  sql = "SELECT * FROM artists"
  results = run_sql(sql)
  for res in results:
    artist = Artist(res["artist_title"], res["id"])
    artists.append(artist)

  return artists

