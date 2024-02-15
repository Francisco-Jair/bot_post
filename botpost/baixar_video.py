from pytube import YouTube


def download_video(url, output_path):
    yt = YouTube(url)
    yt.streams.get_highest_resolution().download(output_path)
    return yt.title
