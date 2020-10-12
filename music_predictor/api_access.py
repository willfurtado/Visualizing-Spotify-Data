##########################
### Spotify API Access ###
##########################

from secrets import CLIENT_USERNAME, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI

import spotipy
import spotipy.util as util

token = util.prompt_for_user_token(CLIENT_USERNAME,
                           "user-library-read",
                           client_id=SPOTIPY_CLIENT_ID,
                           client_secret=SPOTIPY_CLIENT_SECRET,
                           redirect_uri=SPOTIPY_REDIRECT_URI)

sp = spotipy.Spotify(auth=token)


