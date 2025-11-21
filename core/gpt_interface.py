# GPT-OSS interface
from openai import OpenAI
from config.settings import HF_TOKEN
from json import loads

class GPTInterface:
    def __init__(self, model_path):
        self.model_path = model_path
        self.client = OpenAI(
            base_url="https://router.huggingface.co/v1",
            api_key=HF_TOKEN,
        )

    def analyze_code(self, code: str, language: str) -> str:

        output_format = """
        {
            "file": "api/login.py",
            "language": "python",
            "analysis": {
                "vulnerability": "SQL injection due to string concatenation in query",
                "exploit": "Attacker can inject SQL such as ' OR 1=1 -- to bypass login",
                "mitigation": "Use parameterized queries: cursor.execute('SELECT * FROM users WHERE name=?', (name,))"
            }
        }

        """
        response = self.client.chat.completions.create(
            model=self.model_path,
            messages=[{"role": "user", "content": f"Here is a {language} file. can you spot the security vulnerability?! give me the result in the following json format sample (remove the ``` code block): \n" + output_format 
                + f'\n{code}\n'
            }],
        )

        print(response.choices[0].message.content)
        return loads(response.choices[0].message.content)
