from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = "https://www.billboard.com/charts/hot-100/"+date+"/"
URL_REDIRECT = "http://example.com"

SPOTIPY_CLIENT_ID = os.environ["SPOTIFY_ID"]
SPOTIPY_CLIENT_SECRET= os.environ["SPOTIFY_SECRET"]
# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))
spotify = spotipy.oauth2.SpotifyOAuth(client_id = SPOTIPY_CLIENT_ID, 
                                      client_secret = SPOTIPY_CLIENT_SECRET, 
                                      redirect_uri = URL_REDIRECT, scope= "playlist-modify-private")
client = spotipy.client.Spotify(oauth_manager=spotify)
user_id = client.current_user()['id']
print(user_id)

# access_token = spotify.get_access_token()1
# print(access_token)

response = (requests.get(URL)).text
soup = BeautifulSoup(response, "html.parser")
titles = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
# print(titles)

#getting songs titles from billboard website
songs = [title.text.strip() for title in titles]

# getting uris from Spotify for each song's title
uris= [client.search(song)['tracks']['items'][0]['uri'] for song in songs]
print(uris)

create_playlist = client.user_playlist_create(user_id, name=f"Billboard 100 on {date}", public=False, description="My throwback music")
print(create_playlist)
playlist_id = create_playlist["id"]

client.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=uris)





# authors = soup.find_all(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")                      
# # print(authors)
# artists = []
# for artist in authors:
#     author = artist.getText().strip()
#     #  = a.strip()
#     artists.append(author)
# print(artists)   
