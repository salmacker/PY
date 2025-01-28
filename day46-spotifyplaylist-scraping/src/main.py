import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import pprint
from dotenv import find_dotenv, load_dotenv

# Load environement variables
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.environ.get('SPOTIPY_REDIRECT_URI') 

# A - Webscrapper Billboard part
date_question = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date_question}"

response = requests.get(URL, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"})
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

song_names = soup.select("li h3.c-title")
songs_list = [song.getText().strip() for song in song_names]
songs_list = songs_list[:20] 

artists_and_numbers = soup.select("li span.c-label")
artists_and_numbers = [item.get_text(strip=True) for item in artists_and_numbers] 

# Filter out the "-" and "NEW" tags from the artist list
artists_list = [item for item in artists_and_numbers if item not in ('-', 'NEW') and not item.isnumeric()]
artists_list = artists_list[:20]


# B - SPOTIFY PART
# Initialize connection to the Spotify API with the Spotipy library
scope = 'user-library-read playlist-modify-private'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
user_id = sp.current_user()["id"]

# Search for a song
def search_song(music,singer):
    result = sp.search(q=f"{music} {singer}", type='track', limit=1)   
    song_title = result["tracks"]["items"][0]["name"]
    song_artist = result["tracks"]["items"][0]["artists"][0]["name"]
    song_uri = result["tracks"]["items"][0]["uri"]
    return song_uri

# Create a new playlist
playlist_name = f"TOP 20 {date_question}"
new_playlist = sp.user_playlist_create(user=user_id,name=playlist_name, public= False, description="This is an automatically created playlist")
playlistid = new_playlist["id"]

# Add songs to the playlist
i = 0
for song, artist in zip(songs_list,artists_list):
    song_uri = search_song(song,artist)
    sp.user_playlist_add_tracks(user=user_id, playlist_id=playlistid, tracks=[song_uri])
    i += 1
    print(f"{i}/20 - {artist} / {song}")
print(f"Playlist {playlist_name} ready!")