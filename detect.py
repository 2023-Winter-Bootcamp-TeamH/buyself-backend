import torch
import json
import pandas as pd

# Model
model = torch.hub.load('ultralytics/yolov5', 'custom', 'best.pt')  # or yolov5n - yolov5x6, custom
# Images
img = 'Test6.jpeg'  # or file, Path, PIL, OpenCV, numpy, list

# Inference
detections = model(img, size=640)

def object_cords():  # 탐지한 객체들의 좌표와 레이블을 반환해줌
    return json.loads(detections.pandas().xyxy[0].to_json(orient="records"))

oj = pd.DataFrame(object_cords())
oj.to_json('test.json', orient="records")

detections.save()


print(oj.to_json(orient="records"))