from enum import Enum

class Status(Enum):
    NORMAL = 'normal'
    THINK = 'think'
    SPEAK = 'speak'

class ChatGPTStatus(Enum):
    NONE = 0
    TALK = 1
    OBJECTION = 2

class Character(Enum):
    ZUNDAMON = 'zundamon'
    NEKOEMON = 'nekoemon'
    SHAROL = 'sharol'
    SHIMA = 'shima'
    GEORGE ='george'
class DisplayName(Enum):
    ZUNDAMON = 'ずんだもん'
    NEKOEMON = 'ねこえもん'
    SHAROL = 'シャロル'
    SHIMA = 'シマ'
    GEORGE ='こうしろ じょうじ'