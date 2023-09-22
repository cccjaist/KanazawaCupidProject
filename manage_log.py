
MESSAGE_LOG_PATH = 'logs/message_logs/'
ERROR_LOG_PATH = 'logs/error_logs/'

import logzero
import datetime

message_file_name = ''
error_file_name = ''

message_logzero = logzero
error_logzero = logzero

# ログファイルを作成する
def init():
    global message_file_name
    global error_file_name
    now = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M')
    message_file_name = 'message_' + now + '.log'
    error_file_name = 'error_' + now + '.log'

    log_format = '%(message)s'
    formatter = message_logzero.LogFormatter(fmt=log_format)
    message_logzero.formatter(formatter)

# エラーファイルに
def write_error_log(log):
    error_logzero.logfile(ERROR_LOG_PATH + error_file_name)
    error_logzero.logger.debug(log)

def write_message_log(log):
    message_logzero.logfile(MESSAGE_LOG_PATH + message_file_name)
    message_logzero.logger.debug(log)
