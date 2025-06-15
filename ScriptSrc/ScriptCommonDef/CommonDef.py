import queue
from enum import Enum, auto

######################################################
MOVE_DURATION = 0.01            # 鼠标移动时间(秒)
CLICK_DELAY = 0.01              # 点击后延迟(秒)
GAME_WINDOW_TITLE = "《天命西游》 水晶宫"  # 游戏窗口标题
######################################################

######################################################
event_id_queue = queue.Queue(5)
######################################################
class AppEvent(Enum):
    IDEL = (0, "idel")
    HANG_BATTLEFIELD = (1, "hang_battlefield")
    BEAT_MONSTER = (2, "beat_monster")

    def __new__(cls, value, description):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.description = description
        return obj
    
class HangBaEvent(Enum):
    IDEL = (0, "idel")
    PREPARE_SCRAMBLE_BRIDE = (1, "Prepare Scramble Bride")
    SUPPRESS_DEVIL = (2, "Suppress devil")
    HANG_BA_END = (2, "Hang Ba End")

    def __new__(cls, value, description):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.description = description
        return obj

