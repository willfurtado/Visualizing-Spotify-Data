import spotipy
from credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from spotipy.oauth2 import SpotifyOAuth


class SpotifyAccess:
    "Spotify API abstraction using Python ``spotipy`` module"

    def __init__(self, scope):
        self.spotify = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope=scope,
                client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                redirect_uri=REDIRECT_URI,
            )
        )
        self._current_user = self.spotify.get_current_user()

    def __enter__(self):
        "Enabling support for context managers with entrance method."
        return self

    def __exit__(self, type, val, traceback):
        "Enabling support for context managers with exit method to close current connection."
        self.__del__()

    @property
    def current_user(self):
        return self._current_user
