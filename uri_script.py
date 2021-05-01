#!bin/python3
import pandas as pd
import json
import spotipy

from spotipy.oauth2 import SpotifyOAuth

plt.style.use('ggplot')

CLIENT_USERNAME = "willfurtado"
SPOTIPY_CLIENT_ID = "0c58b8f377294e1393b6ff20d1db34fc"
SPOTIPY_CLIENT_SECRET = "12fb3865a39343aba75ec4b118f6adf9"
SPOTIPY_REDIRECT_URI = "https://localhost:8888"

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, 
    client_id=SPOTIPY_CLIENT_ID, 
    client_secret=SPOTIPY_CLIENT_SECRET,
    username='willfurtado',
    redirect_uri=SPOTIPY_REDIRECT_URI))

def load_track_data(src):
    """
    Returns a Pandas DataFrame object with the current listening history 
    from Spotify data pull. The src argument is the folder in which the data is stored.
    """
    with open('personal_data/' + src + '/StreamingHistory0.json') as file:
        data0 = json.load(file)
    with open('personal_data/' + src + '/StreamingHistory1.json') as file:
        data1 = json.load(file)
    with open('personal_data/' + src + '/StreamingHistory2.json') as file:
        data2 = json.load(file)
        
    df0 = pd.DataFrame(data0)
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)
    
    df = df0.append(df1, ignore_index=True).append(df2, ignore_index=True)
    
    return df.sort_values("trackName", ascending=False)['trackName'].unique()

songs = load_track_data("winter20")

def get_spotify_uri(song):
    """Returns the corresponding spotify URI from a given song title"""       
    try:
        search_results = sp.search(q=song, type='track', limit=1)
        print(song, "\t" , search_results['tracks']['items'][0]['id'])
    except (AttributeError, IndexError, TypeError) as err:
        pass

if __name__ == "__main__":
	for song in songs:
		try:
			get_spotify_uri(song)
		except TypeError as err:
			pass


