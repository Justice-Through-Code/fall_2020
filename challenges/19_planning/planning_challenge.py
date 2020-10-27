my_playlist = [{'artist': 'Bilal', 'title': 'Sometimes', 'favorite': False},
               {'artist': 'Chaka Khan', 'title': "I'm Every Woman", 'favorite': False},
               {'artist': 'Chaka Khan', 'title': "Ain't Nobody", 'favorite': False},
               {'artist': 'Parliament',
                   'title': 'Mothership Connection (Star Child)', 'favorite': False},
               {'artist': 'Pink Floyd',
                   'title': 'Another Brick in the Wall', 'favorite': False},
               {'artist': 'Parliament', 'title': 'Unfunky UFO', 'favorite': False},
               {'artist': 'Nina Simone',
                   'title': 'Mississippi Goddamn', 'favorite': False},
               {'artist': 'Nina Simone', 'title': 'Four Women', 'favorite': False},
               {'artist': 'Roberta Flack',
                   'title': 'Killing Me Softly', 'favorite': False},
               {'artist': 'Fugees', 'title': 'Killing Me Softly', 'favorite': False}]

'''
FUNCTIONS BELOW NEED TO BE PSEUDOCODED AND IMPLEMENTED
'''

'''
For Question 1:
function to add songs to a playlist
-takes 2 arguments, playlist (list) and song (dictionary)
-returns nothing
'''


def add_song(playlist, song):
    pass


new_song = {'artist': 'Kendrick Lamar', 'title': 'Alright', 'favorite': False}
add_song(my_playlist, new_song)
# Check print to see if the function worked!
print(my_playlist)

'''
For Question 2:
function to search songs by artist
-takes 2 arguments, playlist (list) and artist_name (a string)
-returns a list of songs in the playlist by that artist
'''


def search_by_artist(playlist, artist_name):
    pass


# Check print to see if the function worked!
print(search_by_artist(my_playlist, 'Pink Floyd'))

'''
For Question 3:
Function to search songs by title
-takes 2 arguments, playlist (list) and song_title (string)
-returns a list including all the songs with the title searched
'''


def search_by_title(playlist, song_title):
    pass


# Check print to see if the function worked!
print(search_by_title(my_playlist, 'Killing Me Softly'))

'''
For Question 4
Function to set the favorite status of a song to True
-takes 3 arguments, playlist (list), song_title (string), artist_name (string)
-returns nothing
'''


def favorite_song(playlist, song_title, artist_name):
    pass


favorite_song(my_playlist, "Ain't Nobody", 'Chaka Khan')
favorite_song(my_playlist, "Four Women", 'Nina Simone')
# Check print to see if the function worked!
print(my_playlist)


'''
For Question 5
Function to create a favorites playlist based on songs that have been favorited using favorite_song function
-takes 1 argument, playlist (list)
-returns list of favorite songs
'''


def create_favorites_playlist(playlist):
    pass


# Check print to see if the function worked!
print(create_favorites_playlist(my_playlist))

'''
For Question 6
Function to shuffle a playlist
-takes 1 argument, playlist (list)
-return nothing

Hint: you can use a numpy function to accomplish this!
'''


def play_shuffle(playlist):
    pass


# Check print to see if the function worked!
print(play_shuffle(my_playlist))
