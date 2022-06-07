import pdb 
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

# album_repository.delete_all()
# artist_repository.delete_all()

artist_1 = Artist("Red Hot Chilli Peppers")
artist_repository.save(artist_1)

artist_2 = Artist("Creedence Clearwater Revival")
artist_repository.save(artist_2)

artist_3 = Artist("Dio")
artist_repository.save(artist_1)

album_1 = Album("Cosmo's Factory", "Roots Rock", artist_2)
album_repository.save(album_1)

album_2 = Album("Holy Diver", "Heavy Metal", artist_3)
album_repository.save(album_2)

album_3 = Album("By the Way", "Alternative Rock", artist_1)
album_repository.save(album_3)

pdb.set_trace()