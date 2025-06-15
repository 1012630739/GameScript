import time
import threading
import ctypes
import win32gui

from ScriptLog import RLog
from ScriptCommonDef import CommonDef
from ScriptTargetScan import TargetScan

from ScriptApp.AppHangBattlefield import HangBattlefield

######################################################
TAG = "app_main"
app_event_old_id = CommonDef.AppEvent.IDEL.value
######################################################

def app_event_change(event_id_param):
    global app_event_old_id

    if app_event_old_id != event_id_param:
        RLog.LOGD(TAG, f"app_event_old_id:{app_event_old_id} change to {event_id_param}")
        app_event_old_id = event_id_param
        CommonDef.event_id_queue.put(app_event_old_id)

def app_center():
    global app_event_old_id

    app_event_new_id = CommonDef.event_id_queue.get()

    if app_event_old_id != app_event_new_id:
        RLog.LOGD(TAG, f"app_event_old_id:{app_event_old_id} change to {app_event_new_id}")

        if app_event_new_id != CommonDef.AppEvent.IDEL.value:
            if app_event_new_id == CommonDef.AppEvent.BEAT_MONSTER.value:
                RLog.LOGD(TAG, f"{CommonDef.AppEvent.BEAT_MONSTER.description}")

            elif app_event_new_id == CommonDef.AppEvent.HANG_BATTLEFIELD.value:
                RLog.LOGD(TAG, f"{CommonDef.AppEvent.HANG_BATTLEFIELD.description}")
                HangBattlefield.hang_battlefield_main()
        else:
            RLog.LOGD(TAG, f"{CommonDef.AppEvent.IDEL.description}")
    else:
        RLog.LOGD(TAG, f"mode set repeat")

def app_main_thread():
    RLog.LOGD(TAG, "app_main_thread start")

    while True:
        app_center()
        time.sleep(2)
        # 目前的逻辑不考虑该线程退出的情况

def activate_game_window():
    """激活游戏窗口到前台"""
    hwnd = win32gui.FindWindow(None, CommonDef.GAME_WINDOW_TITLE)
    if not hwnd:
        raise Exception(f"未找到游戏窗口: {CommonDef.GAME_WINDOW_TITLE}")
    
    # 强力激活窗口
    win32gui.ShowWindow(hwnd, 9)  # SW_RESTORE
    win32gui.SetForegroundWindow(hwnd)
    
    # 线程附加技巧
    foreground_thread = ctypes.windll.user32.GetWindowThreadProcessId(win32gui.GetForegroundWindow(), 0)
    current_thread = ctypes.windll.kernel32.GetCurrentThreadId()
    ctypes.windll.user32.AttachThreadInput(foreground_thread, current_thread, True)
    
    time.sleep(1)  # 等待窗口激活

def app_main():
    RLog.LOGD(TAG, "app_main start")
    # 导入yolo模型
    TargetScan.yolov5_model_import()

    activate_game_window()

    CommonDef.event_id_queue.put(CommonDef.AppEvent.HANG_BATTLEFIELD.value)
    
    app_main_handle = threading.Thread(target=app_main_thread, name="app_main")

    app_main_handle.start()