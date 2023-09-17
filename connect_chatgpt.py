ENV_KEY_NAME = 'OPENAI_API_KEY'

import os
import openai
from dotenv import load_dotenv

def init_chatgpt():
    # envファイルからchatGPTのAPIキーを読み込む
    load_dotenv()
    openai.api_key = os.environ[ENV_KEY_NAME]

    print(os.environ[ENV_KEY_NAME])
