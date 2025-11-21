# Main CLI entry point
from core.code_parser import parse_code
from core.language_detector import detect_language
from core.analyzer import analyze_file
from core.report_generator import generate_report
from utils.file_utils import get_files_recursive
from config.settings import EXT_LANG_MAP
from time import sleep

if __name__ == '__main__':
    code_files = get_files_recursive('data/samples/box2/', EXT_LANG_MAP)
    results = []
    for f in code_files:
        content = parse_code(f)
        lang = detect_language(f)
        analysis = analyze_file(content, lang)
        sleep(3)
        results.append({"file": f, "language": lang, "analysis": analysis})
    generate_report(results)

