######################################################
LOGI_DEFINE = 1 # info log
LOGE_DEFINE = 1 # error log
LOGD_DEFINE = 1 # debug log
######################################################

def LOGI(TAG, LOG):
    if LOGI_DEFINE:
         print(f"[{TAG}] I: {LOG}")

def LOGE(TAG, LOG):
    if LOGE_DEFINE:
        print(f"[{TAG}] E: {LOG}")

def LOGD(TAG, LOG):
    if LOGD_DEFINE:
        print(f"[{TAG}] D: {LOG}")