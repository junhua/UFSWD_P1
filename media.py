import fresh_tomatoes

### Create a data structure (i.e. a Python Class) to store your favorite movies, 
### including movie title, box art URL (or poster URL) and a YouTube link to the movie trailer.

class Movie:
	# fields
	title, poster_image_url, trailer_youtube_url = "", "", ""

	# constructor
	def __init__(self, _title, _poster_image_url, _trailer_youtube_url):
		self.title = _title
		self.poster_image_url = _poster_image_url
		self.trailer_youtube_url = _trailer_youtube_url

	def __str__(self):
		return self.movie_title

### Create multiple instances of that Python Class to represent your favorite movies; 
### group all the instances together in a list.


def main():
	movies =[
		# Bride of Spies
		Movie("Bridge of Spies", "http://ia.media-imdb.com/images/M/MV5BMjIxOTI0MjU5NV5BMl5BanBnXkFtZTgwNzM4OTk4NTE@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=mBBuzHrZBro"),

		# The Walk
		Movie("The Walk", "http://ia.media-imdb.com/images/M/MV5BMTU5MDgyNDgzM15BMl5BanBnXkFtZTgwNDA1MjI0NTE@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=GR1EmTKAWIw"),

		# Everest
		Movie("Everest", "http://ia.media-imdb.com/images/M/MV5BNTgyNzE3NjM0OV5BMl5BanBnXkFtZTgwNTM4Nzk4NTE@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=5ZQVpPiOji0"),
	]

	# Open movies page
	fresh_tomatoes.open_movies_page(movies)


if __name__ == "__main__":
    main()