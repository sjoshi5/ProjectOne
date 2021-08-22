import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

export SPOTIPY_CLIENT_ID='f2018fb393c2424dba2844c31e8e2c18'
export SPOTIPY_CLIENT_SECRET='f4bb9567dafc4625877be647542fd919'
export SPOTIPY_REDIRECT_URI='http://localhost'