from pytube import YouTube

def download_video(url, output_path):
    yt = YouTube(url)
    yt.streams.get_highest_resolution().download(output_path)

# Exemplo de uso
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # URL do vídeo do YouTube
output_path = "./video"  # Diretório onde o vídeo será salvo (atual diretório)

download_video(url, output_path)
