import torch
import time
import pyautogui
from PIL import Image  # 显式导入 Pillow

model = 0

def yolov5_model_import():
    global model
    model = torch.hub.load("./", "custom", "runs/train/exp/weights/best.pt", source="local")

def target_scan(target_name, target_confidence):
    global model

    timeout = 0

    while True:
        # 截屏
        screenshot = pyautogui.screenshot()

        # 扫描目标
        results = model(screenshot)

        detections = results.pandas().xyxy[0]  # 格式: [xmin, ymin, xmax, ymax, confidence, class, name]

        # # 打印所有检测目标的坐标
        # print(detections)

        # 遍历每个检测目标
        for index, row in detections.iterrows():
            xmin, ymin, xmax, ymax = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
            confidence = row['confidence']
            class_name = row['name']

            print(f"目标 {index}: {class_name}, 坐标: [{xmin}, {ymin}, {xmax}, {ymax}], 置信度: {confidence:.2f}")

            if (target_name == class_name) and (confidence >= target_confidence):
                return ((xmin + xmax)/2), ((ymin + ymax)/2)

        time.sleep(1)
        timeout += 1
        if timeout >= 10:
            return 0,0