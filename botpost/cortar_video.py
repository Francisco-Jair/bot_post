import math

from moviepy.editor import VideoFileClip


def split_video_time(input_video, output_prefix, duration):
    # Quebra o video em varias partes com base no tempo

    clip = VideoFileClip(input_video)
    clip_duration = clip.duration

    num_parts = math.ceil(clip_duration / duration)

    for i in range(num_parts):
        start_time = i * duration
        end_time = min((i + 1) * duration, clip_duration)
        output_path = f"{output_prefix}_part{i+1}.mp4"
        clip.subclip(start_time, end_time).write_videofile(output_path)

    clip.close()


def split_video(input_video, output_prefix, num_parts):
    # separa o video em numero de partes selecionadas
    clip = VideoFileClip(input_video)
    duration = clip.duration
    part_duration = duration / num_parts

    for i in range(num_parts):
        start_time = i * part_duration
        end_time = (i + 1) * part_duration
        output_path = f"{output_prefix}_part{i+1}.mp4"
        clip.subclip(start_time, end_time).write_videofile(output_path)

    clip.close()


# Exemplo de uso
# input_video = "video/INDICADOR7.mp4"
# output_prefix = "saida/output_video"
# num_parts = 2
# duration = 30

# os.makedirs("saida", exist_ok=True)

# # split_video(input_video, output_prefix, num_parts)
# split_video_time(input_video, output_prefix, duration)
