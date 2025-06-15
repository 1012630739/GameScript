import time
import pyautogui
import pydirectinput

from ScriptLog import RLog
from ScriptCommonDef import CommonDef
from ScriptTargetScan import TargetScan

######################################################
TAG = "action_lib"
######################################################

# 后续封装好了函数后,需要用JSON调用函数来完成流程性的东西。JSON里面描述了如何完成对应的动作（目前JSON的描述写法还在研究中）
# {
#     "all_step":10,
#     "npc_name": "tian_tian",
#     "click": "pop_up",
#     "game_instance_name": "prepare_scramble_bride_action",
#     "the_task_take": ["task1", "task2"]
# }

def mouse_move(target_name, target_confidence):
    xmid, ymid = TargetScan.target_scan(target_name, target_confidence)
    if (xmid == 0) and (ymid == 0):
        return False
    pyautogui.moveTo(xmid, ymid, duration=CommonDef.MOVE_DURATION)
    return True

def mouse_click(action):
    pydirectinput.mouseDown(button=action)
    time.sleep(CommonDef.CLICK_DELAY)
    pydirectinput.mouseUp(button=action)

def keyboarde_click(action):
    pydirectinput.keyDown(action)
    time.sleep(CommonDef.CLICK_DELAY)
    pydirectinput.keyUp(action)

# 找到目标并点击目标
def target_click(target_name, mouse_direction):
    if mouse_move(target_name, 0.6):
        mouse_click(mouse_direction)
        return True
    else:
        RLog.LOGD(TAG, f"{target_name} not find")
        return False

# npc点击出现弹框
def npc_Dialog_box_Pop_up(npc_name):
    target_click(npc_name, 'left')
    time.sleep(3)
    keyboarde_click('x')
    target_click(npc_name, 'right')

# 进入副本
def game_instance_enter(npc_name, game_instance_name):
    npc_Dialog_box_Pop_up(npc_name)
    if target_click(game_instance_name, 'left'):
        target_click("shi", 'left')

# 任务接取
def the_task_take(npc_name, task_name_list):
    npc_Dialog_box_Pop_up(npc_name)
    for task_name in task_name_list:
        if target_click(task_name, 'left'):
            target_click("ling_qu", 'left')