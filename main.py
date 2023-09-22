
MESSAGE_LOG_PATH = 'logs/message_logs/'
ERROR_LOG_PATH = 'logs/error_logs/'

import logzero
import datetime

message_file_name = ''
error_file_name = ''

# ログファイルを作成する
def init():
    global message_file_name
    global error_file_name
    now = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M')
    message_file_name = 'message_' + now + '.log'
    error_file_name = 'error_' + now + '.log'

# エラーファイルに
def write_error_log(log):
    log_format = '[%(levelname)1.1s %(asctime)s %(funcName)s:%(lineno)d] %(message)s'
    formatter = logzero.LogFormatter(fmt=log_format)
    logzero.formatter(formatter)
    logzero.logfile(ERROR_LOG_PATH + error_file_name)
    logzero.logger.error(log)

def write_message_log(log):
    log_format = '%(message)s'
    formatter = logzero.LogFormatter(fmt=log_format)
    logzero.formatter(formatter)
    logzero.logfile(MESSAGE_LOG_PATH + message_file_name)
    logzero.logger.debug(log)