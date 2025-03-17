import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI

# Autenticação
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope='playlist-modify-private'))

def criar_playlist_top_musics(artist_names):
    # Cria uma nova playlist_
    user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(user_id, "Top Tracks Playlist", public=False)
    playlist_id = playlist['id']
    
    music_ids = []
    
    for artist in artist_names:
        results = sp.search(q='artist:' + artist, type='artist')
        if results['artists']['items']:
            artistas_id = results['artists']['items'][0]['id']
            top_music = sp.artist_top_tracks(artistas_id)
            
            # Adiciona as três músicas mais tocadas;
            for music in top_music['tracks'][:3]:
                music_ids.append(music['id'])
        else:
            print(f"Artista não encontrado: {artist}")
    
    # Adiciona as músicas à playlist
    if music_ids:
        sp.playlist_add_items(playlist_id, music_ids)
        print(f"Músicas adicionadas à playlist '{playlist['name']}' com sucesso!")
    else:
        print("Nenhuma música encontrada para adicionar à playlist.")

if __name__ == "__main__":
    artistas = input("Digite os nomes dos artistas separados por vírgula: ").split(',')
    artistas = [artista.strip() for artista in artistas]  # Remove espaços em branco
    criar_playlist_top_musics(artistas)