import sys
import ctypes

from ScriptLog import RLog
from ScriptApp.AppCenter import AppMain
from ScriptUI import UIMain

######################################################
TAG = "main"
######################################################

def admin_permission_get():
    try:
        ret = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        # 其他错误
        if ret <= 32:
            RLog.LOGE(TAG, f"Administrator permission get fail ret:{ret}")
            return False
        return True
    except Exception as e:
        RLog.LOGE(TAG, f"Administrator get fail: {e}")
        return False

def admin_permission_detect():
    try:
        # 检测用户是否以管理员运行脚本
        if not ctypes.windll.shell32.IsUserAnAdmin():
            # 主动获取管理员权限
            return admin_permission_get()
        else:
            return True
    except:
        RLog.LOGE(TAG, "admin_permission_get run except")
        return False

def main_thread():
    RLog.LOGD(TAG, "main_thread start")
    # 获取管理员权限
    if admin_permission_detect():
        RLog.LOGD(TAG, "admin permission get pass")
        # 调用各自的main去创建各自的线程
        AppMain.app_main()
        UIMain.ui_main()
    else:
        RLog.LOGE(TAG, "admin permission get fail")

if __name__ == "__main__":
    main_thread()
    RLog.LOGD(TAG, "main_thread end")
    exit()