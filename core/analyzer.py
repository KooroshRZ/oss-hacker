# Security analyzer
from core.gpt_interface import GPTInterface
from config.settings import MODEL_PATH


def analyze_file(file_content, language):
    gpt = GPTInterface(MODEL_PATH)
    return gpt.analyze_code(file_content, language)

