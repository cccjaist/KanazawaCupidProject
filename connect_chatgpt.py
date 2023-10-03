OPENAI_API_KEY = 'OPENAI_API_KEY'
OPENAI_ORGANIZATION = 'OPENAI_ORGANIZATION'
CHATGPT_MODEL = 'gpt-3.5-turbo'

QUESTION_TEMPLATE = ('以下の会話内容を聞き、200字以内で適切な返答をしてください。\n')

import os
import openai
from dotenv import load_dotenv

def init():
    # envファイルからchatGPTのAPIキーを読み込む
    load_dotenv()
    openai.api_key = os.environ[OPENAI_API_KEY]
    openai.organization = os.environ[OPENAI_ORGANIZATION]

# chatGPTにメッセージを送り、その返答を受信する
def get_response(message, log):

    ans = ''

    try:
        response = openai.ChatCompletion.create(
            model = CHATGPT_MODEL,
            timeout=30,
            request_timeout = 60,
            messages = [
                {
                    'role': 'system',
                    'content': 'あなたは異なる立場の2人の仲を取り持つ仲人です。'
                },
                {
                    'role': 'user',
                    'content': QUESTION_TEMPLATE + message
                }
            ]
        )
        ans = response['choices'][0]['message']['content']
        log.write_response_log(ans)

    except Exception as e:
        log.write_error_log(e)
    
    return ans
