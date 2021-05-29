from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from spotipy.oauth2 import SpotifyOAuth


web_scrapped = requests.get("https://www.billboard.com/charts/hot-100/2000-08-12")
web_text = web_scrapped.text
soup = BeautifulSoup(web_text,"html.parser")

list_of_song = soup.findAll(name="span",class_="chart-element__information__song text--truncate color--primary")
Client_ID =   "3bdeceec04454292ba319bf862830370"
Client_Secret =  "c6ed1fb633ff4bb5a738b8f5106d5863"
#object_spotify = spotipy.oauth2.SpotifyOAuth(client_id=Client_ID,client_secret=Client_Secret,redirect_uri="http://example.com",cache_path="token.txt",show_dialog=True,scope="playlist-modify-private")




sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id = "3bdeceec04454292ba319bf862830370",
        client_secret='c6ed1fb633ff4bb5a738b8f5106d5863',
        show_dialog=True,

    )
)
user_id = sp.current_user()["id"]