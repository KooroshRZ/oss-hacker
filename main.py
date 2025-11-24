# Main CLI entry point
from core.code_parser import parse_code
from core.language_detector import detect_language
from core.analyzer import analyze_file
from core.report_generator import generate_report
from utils.file_utils import get_files_recursive
from config.settings import EXT_LANG_MAP
from time import sleep
import sys

if __name__ == '__main__':

    code_folder = sys.argv[1]
    output_html = sys.argv[2]

    code_files = get_files_recursive(code_folder, EXT_LANG_MAP)
    results = []

    for f in code_files:
        content = parse_code(f)
        lang = detect_language(f)
        analysis = analyze_file(content, lang)
        sleep(10)
        results.append(analysis)
    generate_report(results, sys.argv[2])

