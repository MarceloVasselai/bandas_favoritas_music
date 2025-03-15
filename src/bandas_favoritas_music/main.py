import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI

def get_top_tracks(artist_name):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                                   client_secret=SPOTIPY_CLIENT_SECRET,
                                                   redirect_uri=SPOTIPY_REDIRECT_URI,
                                                   scope="user-library-read"))

    # Busca o artista_
    results = sp.search(q='artist:' + artist_name, type='artist')
    items = results['artists']['items']
    
    if not items:
        print(f'Artista {artist_name} não encontrado.')
        return []

    artist_id = items[0]['id']

    # Obtém as músicas mais tocadas
    top_tracks = sp.artist_top_tracks(artist_id)
    tracks = top_tracks['tracks'][:3]  # Pega as 3 músicas mais tocadas

    return [track['name'] for track in tracks]

def main():
    bandas = input("Digite uma lista de bandas separadas por vírgula: ").split(',')
    bandas = [banda.strip() for banda in bandas]

    todas_as_musicas = []

    for banda in bandas:
        print(f'Obtendo músicas para a banda: {banda}')
        top_tracks = get_top_tracks(banda)
        if top_tracks:
            todas_as_musicas.extend(top_tracks)

    if todas_as_musicas:
        print("Músicas mais tocadas:")
        for musica in todas_as_musicas:
            print(musica)

        # Embaralha as músicas
        random.shuffle(todas_as_musicas)

        print("\nMúsicas em ordem aleatória:")
        for musica in todas_as_musicas:
            print(musica)

if __name__ == "__main__":
    main()