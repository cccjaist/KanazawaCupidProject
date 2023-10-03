OPENAI_API_KEY = 'OPENAI_API_KEY'
OPENAI_ORGANIZATION = 'OPENAI_ORGANIZATION'
CHATGPT_MODEL = 'gpt-3.5-turbo'

PROMPT_PATH = 'prompt/'
QUESTION_TEMPLATE = ('以下の会話内容を聞き、200字以内で適切な返答をしてください。\n')
global PROMPT

import os
import openai
from dotenv import load_dotenv

def init(my_prompt):
    # envファイルからchatGPTのAPIキーを読み込む
    load_dotenv()
    openai.api_key = os.environ[OPENAI_API_KEY]
    openai.organization = os.environ[OPENAI_ORGANIZATION]

    global PROMPT
    with open(PROMPT_PATH + my_prompt.name + '.txt', encoding='utf-8') as f:
        PROMPT = f.read()

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
                    'content': PROMPT
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
