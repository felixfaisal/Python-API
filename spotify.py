import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os 

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="6c882794d4b644b2b1dc54ce28f3aef3",
                                                           client_secret="66ff0cc00d554202b70cb5bc8a43be06"))

results = sp.search(q='Linkin Park', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])
    
results = sp.artist_top_tracks("https://open.spotify.com/artist/36QJpDe2go2KgaRleHCDTp")
for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
    os.system("gst-launch-1.0 playbin uri="+track['preview_url'])
