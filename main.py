import random

from botpost import create_output_dir, list_all_file_folders
from botpost.baixar_video import download_video
from botpost.cortar_video import split_video_time
from botpost.pesquisar_video import search_videos
from botpost.postar_video import postar_video

TERMO = "futebol"
OUTPUT_VIDEO = "./video"
OUTPUT_VIDEO_PROCESSADO = "video_processado/"
TIME_SPLIT_DEFAULT = random.randrange(30, 120)

create_output_dir(OUTPUT_VIDEO)
create_output_dir(OUTPUT_VIDEO_PROCESSADO)


def main():
    # result_url = search_videos(TERMO)[random.randrange(0, 11)]
    # title = download_video(result_url, OUTPUT_VIDEO)
    # print(title)
    # video_path = f"{OUTPUT_VIDEO}/{list_all_file_folders(OUTPUT_VIDEO)[0]}"
    # split_video_time(video_path, OUTPUT_VIDEO_PROCESSADO, TIME_SPLIT_DEFAULT)
    # print("Video cortado com sucesso!")



if __name__ == "__main__":
    main()
