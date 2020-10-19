'''
THESE FIRST THREE FUNCTIONS ARE FROM LAST CHALLENGE
THEY SHOULD NOT NEED TO BE CHANGED
'''

# prints out what is in your playlist
# takes one argument: 'playlist' (a list)
def display_playlist(playlist):
	if len(playlist) == 0:
		print('Playlist is empty!')
	else:
		for i in range(len(playlist)):
			print(f'Track {i+1}: {playlist[i]["plays"]} plays \
				  \n\t-{playlist[i]["title"]} by {playlist[i]["artist"]}')

# function to add a song to the playlist
# takes two arguments: 'playlist' (a list), and 'song' (a dictionary)
def add_song(playlist, song):
	# automatically initialize play count of song to 0
	song['plays'] = 0
	playlist.append(song)

# function to get the playlist length
# takes 1 argument, the playlist (a list)
# returns an integer for the playlist length
def get_playlist_length(playlist):
	return(len(playlist))


''' 
FUNCTIONS BELOW THIS POINT HAVE PROBLEMS!
'''

'''
For Question 1:
function to search songs by artist
# takes 2 arguments, playlist (list) and artist_name (a string)
# returns a list of songs in the playlist by that artist
# if there are no songs found by that artist, the list will be empty
'''
def search_by_artist(playlist, artist_name):
	songs_found = []
	for song in playlist:
		if artist_name == song['artist']:
			songs_found.append(song['artist'])

	return(songs_found)




'''
For Question 2:
Function to search songs by title
# takes 2 arguments, playlist (list) and song_title (string)
# returns a list including all the songs with the title searched
# if there are no songs with this title, the list will be empty
'''
def search_by_title(playlist, song_title):
	songs_found = []
	for song in playlist:
		if song_title == song['title']:
			songs_found = song
	return(songs_found)



'''
For Question 3
Function to play songs from the playlist on shuffle
-takes 1 argument, playlist (list)
-shuffles playlist and plays the first song (playlist[0])
-prints out which song is playing, and increases 'plays' for that song by 1
-no need to return anything
'''

def play_shuffle(playlist):
	print(f'On shuffle! Now playing {playlist[0]["title"]} by {playlist[0]["artist"]}')
	np.random.shuffle(playlist)
	playlist[0]["plays"] +=1



'''
For BONUS Question 4
Function to remove a song from the playlist by title and artist
-takes 3 arguments, playlist(list), song_title (string), and song_artist ('string')
-if that song is in the playlist, it should remove 1 song matching that title/artist from the list
-if that song is not in the playlist, it should print out 'That song is not in your playlist!'
'''

def remove_song(playlist, song_title, song_artist):
	found_song = False
	for song in playlist:
		if song['title'] == song_title:
			playlist.remove(song)
			found_song = True

	if found_song == True:
		print(f'{song_title} by {song_artist} removed')
	else:
		print(f'{song_title} by {song_artist} is not in your playlist')
