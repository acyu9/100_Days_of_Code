import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
response.raise_for_status()
text = response.text

soup = BeautifulSoup(text, "html.parser")
songs = soup.select(selector="li h3", class_="c-title")
# Strip the extra \n etc from title
titles_list = [song.getText().strip() for song in songs]
# Remove the "account", "chart" etc after the 100 song titles
songs_list = titles_list[0:100]
print(songs_list)

# Authentication with Spotify
sp = spotipy.Spotify(
    auth_manager = SpotifyOAuth(
        scope = "playlist-modify-private",
        redirect_url = "http://example.com",
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        show_dialog = True,
        cache_path = "token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

# Followed solution except for first part