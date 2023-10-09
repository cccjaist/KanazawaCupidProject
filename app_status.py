from enum import Enum

class Status(Enum):
    NORMAL = 'normal'
    THINK = 'think'
    SPEAK = 'speak'

class Character(Enum):
    ZUNDAMON = 'zundamon'

class Prompt(Enum):
    ZUNDAMON = 'zundamon'
    DORAEMON = 'doraemon'
    SHAROL = 'sharol'
    SHIMA = 'shima'
    KENNICHI ='kennichi'

# TODO: あとで整合性合わせる
class DisplayName(Enum):
    ZUNDAMON = 'ずんだもん'
    DORAEMON = 'ねこえもん'
    SHAROL = 'シャロル'
    SHIMA = 'シマ'
    KENNICHI ='こうしろ じょうじ'