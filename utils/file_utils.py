# File utils
import os

def get_files_recursive(directory, extensions=None):
    files_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            if extensions is None or os.path.splitext(file)[1] in extensions:
                files_list.append(os.path.join(root, file))
    return files_list

