# Configuration: model path, API keys, thresholds
from config.tokens import HF_TOKEN

MODEL_PATH = 'openai/gpt-oss-120b:cerebras'
HF_TOKEN =HF_TOKEN
EXT_LANG_MAP = {
    '.py': 'python',
    '.js': 'javascript',
    '.java': 'java',
    '.c': 'c',
    '.cpp': 'cpp',
    '.php': 'php',
    '.go': 'go'
}