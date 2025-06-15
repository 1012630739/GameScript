import time
import threading

from ScriptLog import RLog
from ScriptCommonDef import CommonDef
from ScriptActionLib import ActionLib

######################################################
TAG = "hang_battlefield"

hang_battlefield_thread_creat_flag = 0

hang_ba_event_id = CommonDef.HangBaEvent.PREPARE_SCRAMBLE_BRIDE.value
######################################################

def prepare_scramble_bride_action():
    # 打开图像检测，获取甜甜的坐标位置
    mouse_move("tian_tian", 0.5)
    # 左键点击甜甜，自动跑向甜甜
    mouse_click('left')
    # 等待跑到靠近甜甜的位置
    time.sleep(3)
    # 按下x坐下，防止贴近甜甜的时候找不到目标
    keyboarde_click('x')
    # 打开图像检测，获取甜甜的坐标位置
    mouse_move("tian_tian", 0.5)
    # 右键点击甜甜
    mouse_click('right')
    # 获取抢亲预备战的坐标位置
    for i in range(10):
        mouse_move("qiang_qin_yu_bei", 0.5)
        # 左键点击抢亲预备战
        mouse_click('left')
    # 等待是否进入战场弹框出来
    mouse_move("shi", 0.4)
    # 左键点击"按钮是"
    mouse_click('left')
    # 等待进入抢亲预备战
    time.sleep(60*15)
    # 检测进入到抢亲与备战
    # 检测任务是否完成

def suppress_devil_action():
    # 打开图像检测，获取甜甜的坐标位置
    mouse_move("tian_tian", 0.5)
    # 左键点击甜甜，自动跑向甜甜
    mouse_click('left')
    # 等待跑到靠近甜甜的位置
    time.sleep(3)
    # 按下x坐下，防止贴近甜甜的时候找不到目标
    keyboarde_click('x')
    # 打开图像检测，获取甜甜的坐标位置
    mouse_move("tian_tian", 0.5)
    # 右键点击甜甜
    mouse_click('right')
    # 获取镇魔窟的坐标位置
    for i in range(10):
        mouse_move("zhen_mo_ku", 0.5)
        # 左键点击镇魔窟
        mouse_click('left')
    # 等待是否进入战场弹框出来
    mouse_move("shi", 0.4)
    # 左键点击"按钮是"
    mouse_click('left')
    # 检测进入到镇魔窟
    time.sleep(60*15)
    # 检测任务是否完成

def hang_battlefield_thread():
    global hang_ba_event_id
    while True:
        if hang_ba_event_id == CommonDef.HangBaEvent.PREPARE_SCRAMBLE_BRIDE.value:
            RLog.LOGD(TAG, f"{CommonDef.HangBaEvent.PREPARE_SCRAMBLE_BRIDE.name} start")
            prepare_scramble_bride_action()
            # 如果未完成等待出本后再次进入，如果完成准备进入镇魔窟
            hang_ba_event_id = CommonDef.HangBaEvent.SUPPRESS_DEVIL.value
        elif hang_ba_event_id == CommonDef.HangBaEvent.SUPPRESS_DEVIL.value:
            RLog.LOGD(TAG, f"{CommonDef.HangBaEvent.SUPPRESS_DEVIL.name} start")
            suppress_devil_action()
            # 如果未完成等待出本后再次进入，如果完成则结束挂机战场
            hang_ba_event_id = CommonDef.HangBaEvent.HANG_BA_END.value
        elif hang_ba_event_id == CommonDef.HangBaEvent.HANG_BA_END.value: 
            RLog.LOGD(TAG, f"{CommonDef.HangBaEvent.HANG_BA_END.value}")
            break

        time.sleep(1)

def hang_battlefield_main():
    global hang_battlefield_thread_creat_flag

    RLog.LOGD(TAG, "hang_battlefield_main start")

    if hang_battlefield_thread_creat_flag:
        RLog.LOGD(TAG, "hang_battlefield_thread is creat repeat")
    else:
        hang_battlefield_handle = threading.Thread(target=hang_battlefield_thread, name="hang_battlefield")

        hang_battlefield_handle.start()

        hang_battlefield_thread_creat_flag = 1;
        
    