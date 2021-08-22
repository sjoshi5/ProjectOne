from  helpers import *
import spotipy
from spotipy import SpotifyClientCredentials, util
from IPython.core.display import clear_output

import pandas as pd 
import pandasql as ps 
import time
import sqlite3

def get_data(playlist_id,n):
    tracks,columns = download_playlist(playlist_id,n)
    #If the id if for artist, you must to put specify True to the artist parameter
    #tracks,columns = download_albums('id_of_the_artist_or_the_album',artist=False)
    df1 = pd.DataFrame(tracks,columns=columns)
    return df1