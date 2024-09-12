class Song:
    count = 0
    genres = []
    unique_genres = set()
    artists = []
    unique_artists = set()
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre) -> None:
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, gnr):
        cls.genres.append(gnr)
        cls.unique_genres = set(cls.genres)
        cls.add_to_genre_count(gnr)

    @classmethod
    def add_to_artists(cls, musician):
        cls.artists.append(musician)
        cls.unique_artists = set(cls.artists)
        cls.add_to_artist_count(musician)

    @classmethod
    def add_to_genre_count(cls,gnr):
        if gnr in cls.genre_count:
            cls.genre_count[gnr] += 1
        else:
            cls.genre_count[gnr] = 1

    @classmethod
    def add_to_artist_count(cls,artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


Song("99 Problems", "Jay Z", "Rap")
Song("Halo", "Beyonce", "Pop")
Song("Smells Like Teen Spirit", "Nirvana", "Rock")
Song("Something's in the way", "Nirvana", "Rock")

print(Song.artists)
print(Song.genres)
print(Song.genre_count)
