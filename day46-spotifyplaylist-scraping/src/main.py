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

scope = 'user-library-read playlist-modify-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
user_id = sp.current_user()["id"]


# song = "I WANNA BE YOUR SLAVE"
# artist = "Maneskin"
# result = sp.search(q=f"{song} {artist}", type='track', limit=1)   
# song_title = result["tracks"]["items"][0]["name"]
# song_artist = result["tracks"]["items"][0]["artists"][0]["name"]
# song_uri = result["tracks"]["items"][0]["uri"]
# print(song_title)
# print(song_artist)
# print(song_uri)

# question = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# URL = f"https://www.billboard.com/charts/hot-100/{question}"

# print(URL)

# Write your code below this line 👇

# response = requests.get(URL, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"})
# website_html = response.text

# soup = BeautifulSoup(website_html, "html.parser")
# song_titles = soup.find_all('h3',class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

# songs_list=[songs.text.strip() for songs in song_titles]
# print(songs_list)