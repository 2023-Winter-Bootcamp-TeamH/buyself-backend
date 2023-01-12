import os.path
import re
import torch
import json
import pandas as pd
from flask import jsonify

def object_cords(select_model):  # 탐지한 객체들의 좌표와 레이블을 반환해주는 함수
    return json.loads(select_model.pandas().xyxy[0].to_json(orient="records"))

def get_class(select_model):  # label에서 class 추출하는 함수
    obj = pd.DataFrame(object_cords(select_model)).get("class")

    return obj.to_json(orient="records")

def create_txt(select_model): # 텍스트 파일로 만드는 함수
    with open('class.txt', 'w') as f:
        f.write('\t'.join(get_class(select_model)))

    f = open("class.txt")
    data = f.readlines()

    return re.findall('\d+', data[0])

def get_id(num_line):
    i = 0
    while i < len(num_line):
        num_line[i] += 1
        i += 1
    return num_line

def delet_txt():
    file_path = "class.txt"

    if os.path.exists(file_path):
        os.remove(file_path)


def predict():
    model = torch.hub.load('ultralytics/yolov5', 'custom', 'best.pt')

    # image = get_image(img_name)
    img = 'Test.jpeg'
    select_model = model(img, size=640)

    object_cords(select_model)
    get_class(select_model)
    create_txt(select_model)
    num_line = list(map(int, create_txt(select_model)))

    result = []
    for i in get_id(num_line):
        result.append({'id': i})

    delet_txt()

    return result