import yt_dlp

def download_audio(video_url):
    ydl_opts = {
        'format': 'bestaudio/best',  # Baixar a melhor qualidade de áudio
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Usar FFmpeg para extrair o áudio
            'preferredcodec': 'mp3',  # Converter para MP3
            'preferredquality': '192',  # Qualidade do MP3
        }],
        'outtmpl': './downloads/%(title)s.%(ext)s',  # Diretório de saída
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

if __name__ == '__main__':
    video_urls = [
        'https://www.youtube.com/watch?v=x34icYC8zA0',
        'https://www.youtube.com/watch?v=na8xgu-KLAk'
        # Adicione mais URLs conforme necessário.
    ]

    for url in video_urls:
        download_audio(url)