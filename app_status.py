from enum import Enum

class Status(Enum):
    NORMAL = 'normal'
    THINK = 'think'
    SPEAK = 'speak'

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

class Speaker(Enum):
    # ずんだもん(ノーマル)の声
    ZUNDAMON = 3
    # 小夜の声
    NEKOEMON = 46
    # ナースロボ(ノーマル)の声
    SHAROL = 47
    # 後鬼(人間ver)の声
    SHIMA = 27
    # 雀松朱司(ノーマル)の声
    GEORGE = 52