import os.path
import re
import torch
import json
import pandas as pd

# 탐지한 객체들의 좌표와 레이블을 반환해주는 함수
def object_cords(select_model):
    return json.loads(select_model.pandas().xyxy[0].to_json(orient="records"))

# label에서 class 추출하는 함수
def get_class(select_model):
    obj = pd.DataFrame(object_cords(select_model)).get("class")
    return obj.to_json(orient="records")

# 텍스트 파일로 만드는 함수
def create_txt(select_model):
    with open('class.txt', 'w') as f:
        f.write('\t'.join(get_class(select_model)))
    f = open("class.txt")
    data = f.readlines()
    return re.findall('\d+', data[0])

# 텍스트파일에서 int값으로 class id를 가져오는 함수
def get_id(num_line):
    i = 0
    while i < len(num_line):
        num_line[i] += 1
        i += 1
    return num_line

# 사용한 txt파일 삭제하는 함수
def delete_txt():
    file_path = "class.txt"
    if os.path.exists(file_path):
        os.remove(file_path)

# YOLOv5모델로 이미지 객체 탐지
def predict(img_name):
    model = torch.hub.load('ultralytics/yolov5', 'custom', 'best.pt')

    select_model = model(img_name, size=640)

    object_cords(select_model)
    get_class(select_model)

    create_txt(select_model)
    num_line = list(map(int, create_txt(select_model)))

    result = []
    for i in get_id(num_line):
        result.append({'id': i})
    delete_txt()
    return result