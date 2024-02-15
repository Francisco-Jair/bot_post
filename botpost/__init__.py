import os


def create_output_dir(output_dir):
    os.makedirs(output_dir, exist_ok=True)


def list_all_file_folders(path):
    return os.listdir(path)


def path_abs(path):
    return os.path.abspath(path)
