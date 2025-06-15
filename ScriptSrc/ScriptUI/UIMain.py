import time
import threading

from ScriptLog import RLog
from ScriptCommonDef import CommonDef

######################################################
TAG = "ui"
######################################################

def ui_main_thread():
     num = 0
     RLog.LOGD(TAG, "ui_main_thread start")
     while True:
          # if num % 3 == 0:
          #      RLog.LOGD(TAG, "----3----")
          #      CommonDef.event_id_queue.put(CommonDef.AppEvent.HANG_BATTLEFIELD.value)
          # elif num % 5 == 0:
          #      RLog.LOGD(TAG, "----5----")
          #      CommonDef.event_id_queue.put(CommonDef.AppEvent.BEAT_MONSTER.value)

          # if num >= 50:
          #      num = 0
          # else:
          #      num += 1

          time.sleep(1)

def ui_main():
    RLog.LOGD(TAG, "ui_main start")
    
    ui_main_handle = threading.Thread(target=ui_main_thread, name="ui_main")

    ui_main_handle.start()