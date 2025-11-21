# GPT-OSS interface
from openai import OpenAI
from config.settings import HF_TOKEN

class GPTInterface:
    def __init__(self, model_path):
        self.model_path = model_path
        self.client = OpenAI(
            base_url="https://router.huggingface.co/v1",
            api_key=HF_TOKEN,
        )

    def analyze_code(self, code: str, language: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model_path,
            messages=[{"role": "user", "content": f"Here is a {language} file. can you spot the security vulnerability?! just give me a short answer of the vulnerability plus the possible exploit." 
                + f'\n{code}\n'
            }],
        )

        return response.choices[0].message.content
