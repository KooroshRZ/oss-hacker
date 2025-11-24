#!/bin/bash

# Base project directory
BASE_DIR="gpt_sec_tool"

# Directories to create
DIRS=(
    "$BASE_DIR/config"
    "$BASE_DIR/core"
    "$BASE_DIR/data/samples"
    "$BASE_DIR/data/temp"
    "$BASE_DIR/tests"
    "$BASE_DIR/utils"
)

# Create directories
for dir in "${DIRS[@]}"; do
    mkdir -p "$dir"
done

# Files and content (file_path|content)
FILES=(
"$BASE_DIR/config/settings.py|# Configuration: model path, API keys, thresholds\nMODEL_PATH = 'models/gpt-oss'\n"
"$BASE_DIR/config/logging_config.py|# Logging setup\nimport logging\nlogging.basicConfig(level=logging.INFO)\n"

# Core
"$BASE_DIR/core/gpt_interface.py|# GPT-OSS interface\nclass GPTInterface:\n    def __init__(self, model_path):\n        self.model_path = model_path\n        # TODO: load GPT model\n\n    def analyze_code(self, code: str, language: str) -> str:\n        return 'Analysis result placeholder'\n"
"$BASE_DIR/core/code_parser.py|# Code parser\nimport os\n\ndef parse_code(file_path):\n    with open(file_path, 'r') as f:\n        return f.read()\n"
"$BASE_DIR/core/language_detector.py|# Language detector\nimport os\nEXT_LANG_MAP = {\n    '.py': 'python',\n    '.js': 'javascript',\n    '.java': 'java',\n    '.c': 'c',\n    '.cpp': 'cpp'\n}\n\ndef detect_language(file_path):\n    ext = os.path.splitext(file_path)[1]\n    return EXT_LANG_MAP.get(ext, 'unknown')\n"
"$BASE_DIR/core/analyzer.py|# Security analyzer\nfrom core.gpt_interface import GPTInterface\n\ndef analyze_file(file_content, language):\n    gpt = GPTInterface('models/gpt-oss')\n    return gpt.analyze_code(file_content, language)\n"
"$BASE_DIR/core/report_generator.py|# Report generator\nimport json\n\ndef generate_report(results, output_file='report.json'):\n    with open(output_file, 'w') as f:\n        json.dump(results, f, indent=4)\n"

# Utils
"$BASE_DIR/utils/file_utils.py|# File utils\nimport os\n\ndef get_files_recursive(directory, extensions=None):\n    files_list = []\n    for root, _, files in os.walk(directory):\n        for file in files:\n            if extensions is None or os.path.splitext(file)[1] in extensions:\n                files_list.append(os.path.join(root, file))\n    return files_list\n"
"$BASE_DIR/utils/validators.py|# Validators\nimport os\n\ndef file_exists(file_path):\n    return os.path.exists(file_path)\n"
"$BASE_DIR/utils/helpers.py|# Helper functions\nimport time\n\ndef timer(func):\n    def wrapper(*args, **kwargs):\n        start = time.time()\n        result = func(*args, **kwargs)\n        print(f'Time taken: {time.time() - start:.2f}s')\n        return result\n    return wrapper\n"

# Tests
"$BASE_DIR/tests/test_parser.py|# TODO: add parser tests\n"
"$BASE_DIR/tests/test_analyzer.py|# TODO: add analyzer tests\n"
"$BASE_DIR/tests/test_gpt_interface.py|# TODO: add GPT interface tests\n"

# Main entry
"$BASE_DIR/main.py|# Main CLI entry point\nfrom core.code_parser import parse_code\nfrom core.language_detector import detect_language\nfrom core.analyzer import analyze_file\nfrom core.report_generator import generate_report\nfrom utils.file_utils import get_files_recursive\n\nif __name__ == '__main__':\n    code_files = get_files_recursive('data/samples', ['.py', '.js', '.java', '.c', '.cpp'])\n    results = []\n    for f in code_files:\n        content = parse_code(f)\n        lang = detect_language(f)\n        analysis = analyze_file(content, lang)\n        results.append({\"file\": f, \"language\": lang, \"analysis\": analysis})\n    generate_report(results)\n"

# Requirements
"$BASE_DIR/requirements.txt|torch\ntransformers\n# add GPT-OSS dependencies here\n"
)

# Create files with content
for entry in "${FILES[@]}"; do
    file="${entry%%|*}"
    content="${entry#*|}"
    echo -e "$content" > "$file"
done

echo "Project structure created at '$BASE_DIR'"
