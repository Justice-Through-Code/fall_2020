# Advanced API Challenge

This challenge will help you to practice using APIs. Hopefully, this will prepare you and give you a template for working on your WOW project and beyond!

## Part A: Use the News API to get top headlines about vaccines

The goal of this part is to use the News API to search news articles that involve 'vaccine' in the headline to look at all of the titles together

### 1. Get your API key for the News API loaded in to set up an instance of the newsapi client


```python
from newsapi import NewsApiClient
with open('news_api_key.txt') as file:
   api_key = file.read()

news_api = NewsApiClient(api_key)
```

### 2. Use the News API to get just **top headlines** from all sources including the word 'Vaccine'

**Hint**: Check out the [docs](https://newsapi.org/docs/client-libraries/python) for a function you can use to pull top headlines specifically

**Hint2**: You can specify what words need to be included with the parameter `q`


```python
headline_results = news_api.get_top_headlines(q="Vaccine")

```

### 3. Put the titles of all the articles from the results of #2 into a list, and print the list out

**Hint:** It may be helpful to reference the `get_article_titles()` function from the lesson today...


```python
def get_article_titles(results):
    titles = []
    for article in results['articles']:
        titles.append(article['title'])
    return titles
```


```python
get_article_titles(headline_results)

```




    ["Pfizer's vaccine strongly protects against COVID-19, U.S. regulator confirms | CBC News",
     'Watch Live: Fauci speaks with Black leaders about COVID-19 vaccines',
     'Trump takes another vaccine victory lap as US COVID-19 cases rise',
     'Biden vows to distribute 100 million vaccine doses in first 100 days',
     '81-year-old man named William Shakespeare is second person in the U.K. to receive COVID-19 vaccine',
     "Coronavirus Australia live news: Fauci says COVID-19 vaccine 'weeks away' for US as Biden pledges 100m shots in first 100 days in office",
     "Jake Tapper calls President Donald Trump's vaccine remarks 'stunning' - CNN Video",
     'Dr. Anthony Fauci Skips Donald Trump Coronavirus Vaccine Event',
     'Staten Island doctor weighs in on vaccine as cases surge in NYC borough',
     'Joe Biden Pledges to Distribute 100 Million COVID Vaccines in First 100 Days',
     "Trump says coronavirus vaccines to 'end the pandemic,' touts progress as 'modern-day miracle'",
     'Donald Trump Suggests Using Defense Production Act for Coronavirus Vaccines',
     'ASX to advance; UK begins vaccine rollout',
     'Trump orders Americans receive priority access to COVID-19 vaccines',
     "Ottawa says it's not alarmed by Trump's threat to restrict vaccine exports | CBC News",
     "Trump says coronavirus vaccines to 'end the pandemic,' touts progress as 'modern-day miracle'",
     'Are we seeing light at the end of the tunnel for coronavirus?',
     'Thousands of Britons receive world’s first approved coronavirus vaccine',
     'Coronavirus updates: US reaches 15 million infections; Russians must choose between booze and vaccine; Ohio-State Michigan football is off',
     'Republicans Spar Over Ron Johnson Inviting COVID Vaccine Skeptic to Senate Hearing']



## Part B: Get the top 10 tracks for Kendrick Lamar on Spotify using the `spotipy` API:

This part of the challenge is meant to be more abstract and challenging than the first part -- we are giving you far less specific instruction on how to do this, so you'll have to use the [documentation](https://spotipy.readthedocs.io/en/2.13.0/) much more. This piece of the challenge is more like something you'd need to do for your WOW project with an API, good luck!


Import libraries and set up `client_id` and `client_secret` for spotipy


```python
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

with open('spotify_secrets.json') as file:
    secrets = json.load(file)
    
# set up the credentials with the client_id and client_secret
creds = SpotifyClientCredentials(secrets['client_id'], secrets['client_secret'])

# instantiate a spotipy client with the credentials
sp = spotipy.Spotify(client_credentials_manager=creds)
```

Define a function to pull an artist ID by searching that artist on spotify
* then take the 'id' value for the first artist in the list of artists (should be the right match)
* return the artist ID


```python
def get_artist_id(artist_name):
    results = sp.search(q=artist_name, type='artist')
    return results['artists']['items'][0]['id']
```


```python
# get artist id for kendrick lamar
kendrick_id = get_artist_id('Kendrick Lamar')
```

define function to make a list of the top 10 tracks for an artist_id


```python
def get_tracks(artist_id):
    # use spotipy to get top tracks
    results = sp.artist_top_tracks(artist_id, country="US")
    
    # parse resulting dictionary to make a list of the track names
    tracks = []
    for track in results['tracks']:
        tracks.append(track['name'])
    return tracks

```


```python
get_tracks(kendrick_id)
```




    ['HUMBLE.',
     'All The Stars (with SZA)',
     'LOVE. FEAT. ZACARI.',
     'DNA.',
     'Money Trees',
     'Pray For Me (with Kendrick Lamar)',
     'King Kunta',
     'Alright',
     'Swimming Pools (Drank)',
     'HUMBLE. - SKRILLEX REMIX']



## Part C (BONUS). Get the top 10 tracks for a different artist of your choice

This is to make sure that your spotipy code is clean enough to reuse for a different artist! Print out their top 10 spotify tracks in the same way


```python
# Top 10 tracks for Flying Lotus
get_tracks(get_artist_id('Flying Lotus'))
```




    ['Never Catch Me',
     'Black Balloons Reprise - Instrumental',
     'Black Balloons Reprise',
     'More',
     'Massage Situation',
     'Do The Astral Plane',
     'Zodiac Shit',
     'The Climb',
     'Spontaneous',
     'Land Of Honey']


