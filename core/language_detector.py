# Language detector
import os
from config.settings import EXT_LANG_MAP

def detect_language(file_path):
    ext = os.path.splitext(file_path)[1]
    return EXT_LANG_MAP.get(ext, 'unknown')

