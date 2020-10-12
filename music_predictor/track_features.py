######################
### Track Features ###
######################

from api_access import sp
from spotify_personal_data import music, podcasts
from secrets import DIFFICULT_SONGS, UNSEARCHABLE_SONGS
import pandas as pd

import spotipy
import spotipy.util as util

def get_spotify_uri(song):
	"""Uses Spotify API to search for song URI using English title"""
	if song in DIFFICULT_SONGS:
		search_results = sp.search(q=DIFFICULT_SONGS[song], type='track', limit=1)
	else:
		search_results = sp.search(q=song, type='track', limit=1)
	try: 
		return search_results['tracks']['items'][0]['id']
	except (IndexError, AttributeError) as err:
		print('Something went wrong with {}'.format(song))
		pass

def get_song_features(uri):
	"""Uses Spotify API to search for song features using track URI"""
	try:
		features = sp.audio_features([uri])[0]
		return features
	except:
		print("Can't get features for URI: {}".format(uri))

unique_songs = music.groupby('trackName').count().sort_values('secPlayed', ascending=False).index[:1500]

column_labels = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 
	  			'instrumentalness', 'liveness', 'valence', 'tempo', 'type', 'id', 'uri', 'track_href', 
	  			'analysis_url', 'duration_ms', 'time_signature']

features_df = pd.DataFrame(columns=column_labels)

for song in unique_songs:
	uri = get_spotify_uri(song)
	features = get_song_features(uri)
	dataframe = pd.DataFrame(data=features, index=[song])
	features_df = features_df.append(dataframe)

features_df.to_csv('../features/features2.csv', index=True)