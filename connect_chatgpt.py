import os
import openai
from dotenv import load_dotenv
from app_status import ChatGPTStatus as status

OPENAI_API_KEY = 'OPENAI_API_KEY'
OPENAI_ORGANIZATION = 'OPENAI_ORGANIZATION'
CHATGPT_MODEL = 'gpt-4'

PROMPT_PATH = 'prompt/'

QUESTION_TEMPLATE = {
    status.TALK : ('以下は、2人の会話内容です。あなたはファシリテーターとして、200字以内で適切な返答をしてください。\n'),
    status.OBJECTION : ('以下の文章に対して、200字以内で反論してください。')
}

global PROMPT

def init(my_prompt):
    # envファイルからchatGPTのAPIキーを読み込む
    load_dotenv()
    openai.api_key = os.environ[OPENAI_API_KEY]
    openai.organization = os.environ[OPENAI_ORGANIZATION]

    global PROMPT
    with open(PROMPT_PATH + my_prompt + '.ini', encoding='utf-8') as f:
        PROMPT = f.read()

# chatGPTにメッセージを送り、その返答を受信する
def get_response(message, status, log):

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
                    'content': QUESTION_TEMPLATE[status.OBJECTION] + message
                }
            ]
        )
        ans = response['choices'][0]['message']['content']
        log.write_response_log(ans)
    
        if ans == 'ERROR: Terminate response.':
            ans = '質問が悪かったようです。もう一度、分かりやすく質問してくれますか。'

    except Exception as e:
        log.write_error_log(e, 3)
    
    return ans
