OPENAI_API_KEY = 'OPENAI_API_KEY'
OPENAI_ORGANIZATION = 'OPENAI_ORGANIZATION'
CHATGPT_MODEL = 'gpt-3.5-turbo'

QUESTION_TEMPLATE = ('以下の2人の会話内容を聞いて、200字以内で返答してください。\n')

import os
import openai
import manage_log as log
from dotenv import load_dotenv

def init():
    # envファイルからchatGPTのAPIキーを読み込む
    load_dotenv()
    openai.api_key = os.environ[OPENAI_API_KEY]
    openai.organization = os.environ[OPENAI_ORGANIZATION]

# chatGPTにメッセージを送り、その返答を受信する
def get_response(message):

    # TODO: 本番ではここのreturnを消去する
    return 'ほげほげ'

    res = openai.ChatCompletion.create(
        model = CHATGPT_MODEL,
        messages = [
            {
                'role': 'system',
                'content': 'あなたは異なる立場の2人の仲を取り持つ仲介人です。'
            },
            {
                'role': 'user',
                'content': QUESTION_TEMPLATE + message
            }
        ]
    )

    ans = res['choices'][0]['message']['content']
    return ans
