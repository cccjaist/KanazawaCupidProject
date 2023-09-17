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
                'role': 'user',
                'content': text
            }
        ]
    )

    # TODO : クレジットの登録が必要
    # URL: https://qiita.com/kotattsu3/items/d6533adc785ee8509e2c
    ans = res.choices[0].text.strip()
    return ans

