import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI

# Autenticação
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope='playlist-modify-private'))

def criar_playlist_top_musics(artist_names):
    # Cria uma nova playlist
    user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(user_id, "Top Tracks Playlist", public=False)
    playlist_id = playlist['id']
    
    track_ids = []
    
    for artist in artist_names:
        results = sp.search(q='artist:' + artist, type='artist')
        if results['artists']['items']:
            artist_id = results['artists']['items'][0]['id']
            top_tracks = sp.artist_top_tracks(artist_id)
            
            # Adiciona as três músicas mais tocadas
            for track in top_tracks['tracks'][:3]:
                track_ids.append(track['id'])
        else:
            print(f"Artista não encontrado: {artist}")
    
    # Adiciona as músicas à playlist
    if track_ids:
        sp.playlist_add_items(playlist_id, track_ids)
        print(f"Músicas adicionadas à playlist '{playlist['name']}' com sucesso!")
    else:
        print("Nenhuma música encontrada para adicionar à playlist.")

if __name__ == "__main__":
    artistas = input("Digite os nomes dos artistas separados por vírgula: ").split(',')
    artistas = [artista.strip() for artista in artistas]  # Remove espaços em branco
    criar_playlist_top_musics(artistas)