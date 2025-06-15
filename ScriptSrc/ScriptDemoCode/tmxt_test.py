import torch
import pyautogui
from PIL import Image  # 显式导入 Pillow

model = torch.hub.load("./", "custom", "runs/train/exp/weights/best.pt", source="local")

# 截屏
screenshot = pyautogui.screenshot()

# 扫描目标
results = model(screenshot)

detections = results.pandas().xyxy[0]  # 格式: [xmin, ymin, xmax, ymax, confidence, class, name]

# 打印所有检测目标的坐标
print(detections)

# 遍历每个检测目标
for index, row in detections.iterrows():
    xmin, ymin, xmax, ymax = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
    confidence = row['confidence']
    class_name = row['name']
    
    print(f"目标 {index}: {class_name}, 坐标: [{xmin}, {ymin}, {xmax}, {ymax}], 置信度: {confidence:.2f}")
    