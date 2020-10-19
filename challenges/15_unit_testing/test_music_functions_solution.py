'''
We are working with music playlists again today!
This time, we've written all the functions for you...but we've made some mistakes

Your challenge today is to do something called 'unit testing' 
This means you should test the individual functions to figure ouw how they're broken
-Do they give the correct outputs for a variety of inputs?
-If they don't give the correct outputs, then your challenge is to fix the function!

All the functions are defined in music_playlist_functions.py
You'll import and run the functions to test them out in this script!

Remember from last time:
-the playlist is a LIST made up of 1 DICTIONARY for each song
-each song dictionary in the playlist has key-value pairs for artist, title, and plays
'''


# SETUP
from music_playlist_functions_solution import *

my_music = []

# add a bunch of songs to the playlist
my_songs = [{'artist': 'Bilal', 'title': 'Sometimes'},
			{'artist': 'Chaka Khan', 'title': "I'm Every Woman"},
			{'artist': 'Chaka Khan', 'title': "Ain't Nobody"},
			{'artist': 'Parliament', 'title': 'Mothership Connection (Star Child)'},
			{'artist': 'Pink Floyd', 'title': 'Another Brick in the Wall'},
			{'artist': 'Parliament', 'title': 'Unfunky UFO'},
			{'artist': 'Nina Simone', 'title': 'Mississippi Goddamn'},
			{'artist': 'Nina Simone', 'title': 'Four Women'},
			{'artist': 'Roberta Flack', 'title': 'Killing Me Softly'},
			{'artist': 'Fugees', 'title': 'Killing Me Softly'}]
# add songs in a loop
for song in my_songs:
	add_song(my_music, song)

# display the whole playlist
display_playlist(my_music)

'''
1. Test out the search_by_artist() function
This function should take as arguments the playlist and an artist
It should return a list of all songs in the playlist by that artist
For example: search_by_artist(my_music, 'Nina Simone') should return
['Mississippi Goddamn', 'Four Women']
'''
# TODO: test out the search_by_artist() function and fix any problems
print('QUESTION 1\n')
print(search_by_artist(my_music, 'Nina Simone'))
print(search_by_artist(my_music, 'Parliament'))

# SOLUTION: the function as written is returning the artist value from the song dictionaries
# On line 45, it should be: songs_found.append(song['title'])

'''
2. Test out the search_by_title() function
This function should take as arguments the playlist and a song title
It should return a list containing the info for all songs in the playlist matching that title

For example: search_by_title(my_music, 'Unfunky UFO') should return
[{'artist': 'Parliament', 'title': 'Unfunky UFO', 'plays': 0}]


Another example: search_by_title(my_music, 'Killing Me Softly') should return:
[{'artist': 'Roberta Flack', 'title': 'Killing Me Softly', 'plays': 0}, {'artist': 'Fugees', 'title': 'Killing Me Softly', 'plays': 0}]
'''


# TODO: test out the search_by_title() function and fix any problems
print('QUESTION 2\n')
print(search_by_title(my_music, 'Unfunky UFO'))
print(search_by_title(my_music, 'Killing Me Softly')) # should note here that this only returns 1 song

# SOLUTION: if it finds a matching title, the function currently assigns the song dictionary itself to songs_found
# Instead, the song dictionary should be appended to the list songs_found
# line 63 should be: songs_found.append(song)


'''
3. Test out the function play_shuffle() function
This function takes 1 argument, playlist
-It should shuffle the playlist randomly using np.random.shuffle() 
-Then, it should play the first song in the playlist (at list index 0) and print out which song
-It should ALSO increase the 'plays' count of that same song by 1

For example, if you run play_shuffle(my_music), you might see:
On shuffle! Unfunky UFO by Parliament


Or you could see: 
On shuffle! Killing Me Softly by Roberta Flack

If you run the function multiple times, you should see that it is playing different songs. 

Also, after shuffling, you can run display_playlist() again 
-you should see the new song order and which songs have been played
'''

# TODO: test out the play_shuffle() function and fix any problems
print('QUESTION 3\n')

play_shuffle(my_music)
play_shuffle(my_music)
play_shuffle(my_music)
display_playlist(my_music)

# SOLUTION: Lines 78 and 79 should be swapped in order. 
# Right now, the function prints which song is playing BEFORE shuffling the playlist
# It should be shuffled first, before playing the song



'''
BONUS Question 4. Test out the remove_song() function
This function takes 3 arguments, playlist (list), song_title (string), and song_artist (string)
-It should remove the song matching both the title and the artist
-If it can't find the song, it will print a message saying so

For example, running remove_song(my_music, song_title = 'Killing Me Softly', song_artist = 'Fugees')
You should get

Killing Me Softly by Fugees removed

Then when you run display_playlist(my_music), you should see this song is gone
'''

# TODO: Make sure the remove_song() function is working
# HINT: use the display_playlist() function after removing songs to make sure the song you want to remove is gone
# HINT: Make sure that ONLY the specific song you want to remove (matching title AND artist) has been removed
print('BONUS QUESTION 4\n')

remove_song(my_music, song_title = 'Killing Me Softly', song_artist = 'Fugees')
display_playlist(my_music)

# SOLUTION: The function is currently removing all songs matching the input song_title
# It needs to check that the artist matches too
# Otherwise, in this example, it will remove ALL versions of 'Killing Me Softly', not just the Fugees
# line 95 should have an and statement and a second condition for the artist: 
# ---    if song['title'] == song_title and song['artist'] == song_artist:

'''
Homework: comment the code & push to Github!
The functions in music_playlist.functions.py don't really have any comments
-For homework, go through these functions and make sure you can convince yourself you understand what each piece does
-Add comments to any lines of the code in these functions where it wasn't immediately obvious to you what it did 


Remember to add, commit, and push your work to Github after you are done!
'''