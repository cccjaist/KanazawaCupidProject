MESSAGE_LOG_PATH = 'logs/message_logs/'
ERROR_LOG_PATH = 'logs/error_logs/'

import os
import logzero
import datetime

global message_file_name
global tmp_message_file_name
error_file_name = ''

message_logzero = logzero
error_logzero = logzero

# ログファイルを作成する
def init():
    global message_file_name
    global tmp_message_file_name
    global error_file_name
    now = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M')
    message_file_name = 'message_' + now + '.log'
    tmp_message_file_name = 'message_' + now + '_tmp.log'
    error_file_name = 'error_' + now + '.log'

    log_format = '%(message)s'
    formatter = message_logzero.LogFormatter(fmt=log_format)
    message_logzero.formatter(formatter)

# エラー情報をログに追加する
def write_error_log(log):
    print(log)
    error_logzero.logfile(ERROR_LOG_PATH + error_file_name, encoding='utf-8')
    error_logzero.logger.debug(log)

# 会話内容をtmpファイルに追加する
def write_message_log(log):
    message_logzero.logfile(get_tmp_file_name(), encoding='utf-8')
    message_logzero.logger.debug(log)

# tmpファイルの会話内容をリセットしlogに統合する
def attach_message_log():
    message = ''
    with open(get_tmp_file_name(), 'r', encoding='utf-8') as f:
        message = f.read()
    with open(get_tmp_file_name(), 'w', encoding='utf-8') as f:
        f.write('')
    message_logzero.logfile(MESSAGE_LOG_PATH + message_file_name, encoding='utf-8')
    message_logzero.logger.debug(message)

# ログのファイル名を取得する
def get_tmp_file_name():
    return MESSAGE_LOG_PATH + tmp_message_file_name

# tmpファイルを削除する
def delete_tmp_file():
    attach_message_log()
    os.remove(get_tmp_file_name())