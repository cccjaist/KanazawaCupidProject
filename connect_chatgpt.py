OPENAI_API_KEY = 'OPENAI_API_KEY'
OPENAI_ORGANIZATION = 'OPENAI_ORGANIZATION'
CHATGPT_MODEL = 'gpt-3.5-turbo'

import os
import openai
from dotenv import load_dotenv

def init():
    # envファイルからchatGPTのAPIキーを読み込む
    load_dotenv()
    openai.api_key = os.environ[OPENAI_API_KEY]
    openai.organization = os.environ[OPENAI_ORGANIZATION]

def get_response(text):

    res = openai.ChatCompletion.create(
        model = CHATGPT_MODEL,
        messages = [
            {
                'role': 'system',
                'content': '日本語で会話してください'
            },
            {
                'role': 'user',
                'content': text
            }
        ]
    )

    ans = res['choices'][0]['message']['content']
    return ans

