
import json

from elasticsearch import Elasticsearch
from flask import jsonify

def inputData():
    es = Elasticsearch("http://elastic:9200/")

    if es.indices.exists(index='dictionary'):
        return
    else:
        es.indices.create(
            index='dictionary',
            body={
                "settings": {
                    "index": {
                        "analysis": {
                            "analyzer": {
                                "nori_token": {
                                    "type": "custom",
                                    "tokenizer": "nori_tokenizer"
                                }
                            }
                        }
                    }
                },
                "mappings": {
                    "properties": {
                        "class_name": {
                            "type": "text",
                            "analyzer": "nori_token"
                        },
                        "price": {
                            "type": "integer",
                        },
                        "img_url": {
                            "type": "text",
                        }
                    }
                }
            }
        )

    json_data = [
  {
    "class_name": "페레로)페레로로쉐",
    "price": 6500,
    "img_url": "https://buyself.s3.ap-northeast-2.amazonaws.com/allProductImage/%ED%8E%98%EB%A0%88%EB%A1%9C)%ED%8E%98%EB%A0%88%EB%A1%9C%EB%A1%9C%EC%89%90100G.jpg"
  },
    {
    "class_name": "코카)환타 오렌지",
    "price": 700,
    "img_url": "https://buyself.s3.ap-northeast-2.amazonaws.com/allProductImage/%EC%BD%94%EC%B9%B4)%ED%99%98%ED%83%80%EC%98%A4%EB%A0%8C%EC%A7%80185ML.jpg"
  },
    {
    "class_name": "오리온)촉촉한 초코칩",
    "price": 2430,
    "img_url": "https://buyself.s3.ap-northeast-2.amazonaws.com/allProductImage/%EC%98%A4%EB%A6%AC%EC%98%A8%EC%B4%89%EC%B4%89%ED%95%9C%EC%B4%88%EC%BD%94%EC%B9%A9240G.jpg"
  },
    {
    "class_name": "코카)스프라이트",
    "price": 1000,
    "img_url": "https://buyself.s3.ap-northeast-2.amazonaws.com/allProductImage/%EC%BD%94%EC%B9%B4)%EC%8A%A4%ED%94%84%EB%9D%BC%EC%9D%B4%ED%8A%B8355ml.jpg"
  },
  {
    "class_name": "롯데)트레비 레몬",
    "price": 1200,
    "img_url": "https://buyself.s3.ap-northeast-2.amazonaws.com/allProductImage/%EB%A1%AF%EB%8D%B0%ED%8A%B8%EB%A0%88%EB%B9%84%EB%A0%88%EB%AA%AC(500ml).jpg"
  },
  {
    "class_name": "서울)짜요짜요 복숭아",
    "price": 2450,
    "img_url": "https://buyself.s3.ap-northeast-2.amazonaws.com/allProductImage/%EC%84%9C%EC%9A%B8_%EC%A7%9C%EC%9A%94%EC%A7%9C%EC%9A%94%EC%9A%94%EA%B5%AC%EB%A5%B4%ED%8A%B8%EB%B3%B5%EC%88%AD%EC%95%84_240G.jpg"
  },
  {
    "class_name": "서울)짜요짜요 포도",
    "price": 2450,
    "img_url": "https://buyself.s3.ap-northeast-2.amazonaws.com/allProductImage/%EC%84%9C%EC%9A%B8_%EC%A7%9C%EC%9A%94%EC%A7%9C%EC%9A%94%EC%9A%94%EA%B5%AC%EB%A5%B4%ED%8A%B8%ED%8F%AC%EB%8F%84_240G.jpg"
  },
  {
    "class_name": "쁘띠젤)화이트 코코",
    "price": 1850,
    "img_url": "https://buyself.s3.ap-northeast-2.amazonaws.com/allProductImage/%EC%81%98%EB%9D%A0%EC%A0%A4(%EC%9A%94%EA%B1%B0%ED%8A%B8%EC%A0%A4%EB%A6%AC%ED%99%94%EC%9D%B4%ED%8A%B8%EC%BD%94%EC%BD%94).jpg"
  },
  {
    "class_name": "쁘띠젤)블루베리",
    "price": 1850,
    "img_url": "https://buyself.s3.ap-northeast-2.amazonaws.com/allProductImage/%EC%81%98%EB%9D%A0%EC%A0%A4(%EC%9A%94%EA%B1%B0%ED%8A%B8%EB%B8%94%EB%A3%A8%EB%B2%A0%EB%A6%AC).jpg"
  },
  {
    "class_name": "쁘띠젤)밀감",
    "price": 1850,
    "img_url": "https://buyself.s3.ap-northeast-2.amazonaws.com/allProductImage/%EC%81%98%EB%9D%A0%EC%A0%A4(%EB%B0%80%EA%B0%90).jpg"
  },
  {
    "class_name": "해태)코코팜 화이트",
    "price": 500,
    "img_url": "https://buyself.s3.ap-northeast-2.amazonaws.com/allProductImage/%EC%BD%94%EC%BD%94%ED%8C%9C%ED%99%94%EC%9D%B4%ED%8A%B8%EC%9A%94%EA%B5%AC%EB%A5%B4%ED%8A%B8.jpg"
  },
  {
    "class_name": "롯데)오가닉 사과 당근",
    "price": 900,
    "img_url": "https://buyself.s3.ap-northeast-2.amazonaws.com/allProductImage/%ED%8C%8C%EC%8A%A4%ED%87%B4%EB%A5%B4%EC%98%A4%EA%B0%80%EB%8B%89%EC%9C%A0%EA%B8%B0%EB%86%8D%EC%82%AC%EA%B3%BC_%EB%8B%B9%EA%B7%BC+125ML.jpg"
  },
  {
    "class_name": "동아)포카리스웨트",
    "price": 2050,
    "img_url": "https://buyself.s3.ap-northeast-2.amazonaws.com/allProductImage/%EB%8F%99%EC%95%84%ED%8F%AC%EC%B9%B4%EB%A6%AC%EC%8A%A4%EC%9B%A8%ED%8A%B8620ml.jpg"
  },
  {
    "class_name": "동서)제티 초코",
    "price": 400,
    "img_url": "https://buyself.s3.ap-northeast-2.amazonaws.com/allProductImage/%EB%8F%99%EC%84%9C%EC%A0%9C%ED%8B%B0%EC%B4%88%EC%BD%94175ML.jpg"
  },
  {
    "class_name": "SFC)수박 소다",
    "price": 850,
    "img_url": "https://buyself.s3.ap-northeast-2.amazonaws.com/allProductImage/%EC%88%98%EB%B0%95%EC%86%8C%EB%8B%A4350ML.jpg"
  },
  {
    "class_name": "쥬맥스)모구모구 리치",
    "price": 1500,
    "img_url": "https://buyself.s3.ap-northeast-2.amazonaws.com/allProductImage/%ED%95%9C%EA%B5%AD%EC%A5%AC%EB%A7%A5%EC%8A%A4)%EB%AA%A8%EA%B5%AC%EB%AA%A8%EA%B5%AC%EB%A6%AC%EC%B9%98%EB%A7%9B.jpg"
  },
  {
    "class_name": "이마트)피코크 망고",
    "price": 2980,
    "img_url": "https://buyself.s3.ap-northeast-2.amazonaws.com/allProductImage/%EC%9D%B4%EB%A7%88%ED%8A%B8%ED%94%BC%EC%BD%94%ED%81%AC%EB%A7%9D%EA%B3%A0%EA%B7%B8%EB%8C%80%EB%A1%9C10G.jpg"
  },
  {
    "class_name": "롯데)말랑카우 딸기",
    "price": 3980,
    "img_url": "https://buyself.s3.ap-northeast-2.amazonaws.com/allProductImage/%EB%A1%AF%EB%8D%B0%ED%91%B9%EC%8B%A0%ED%91%B9%EC%8B%A0%EB%A7%90%EB%9E%91%EC%B9%B4%EC%9A%B0%EB%94%B8%EA%B8%B0%EC%9A%B0%EC%9C%A0.jpg"
  },
  {
    "class_name": "나무)오렌지모양 캔디",
    "price": 1000,
    "img_url": "https://buyself.s3.ap-northeast-2.amazonaws.com/allProductImage/%EB%82%98%EB%AC%B4%EC%9D%B8%ED%84%B0%EB%84%A4%EC%85%9C%EB%84%90%EC%98%A4%EB%A0%8C%EC%A7%80%EB%AA%A8%EC%96%91%EC%BA%94%EB%94%94%EB%B0%95%EC%8A%A425G.jpg"
  },
  {
    "class_name": "오리온)후레쉬베리",
    "price": 5760,
    "img_url": "https://buyself.s3.ap-northeast-2.amazonaws.com/allProductImage/%EC%98%A4%EB%A6%AC%EC%98%A8%ED%9B%84%EB%A0%88%EC%89%AC%EB%B2%A0%EB%A6%AC%EB%94%B8%EA%B8%B0336G.jpg"
  },
  {
    "class_name": "크라운)마이쮸 사과",
    "price": 2080,
    "img_url": "https://buyself.s3.ap-northeast-2.amazonaws.com/allProductImage/%ED%81%AC%EB%9D%BC%EC%9A%B4)%EB%A7%88%EC%9D%B4%EC%AE%B8%EC%82%AC%EA%B3%BC110G.jpg"
  },
  {
    "class_name": "크라운)마이쮸 포도",
    "price": 2080,
    "img_url": "https://buyself.s3.ap-northeast-2.amazonaws.com/allProductImage/%ED%81%AC%EB%9D%BC%EC%9A%B4)%EB%A7%88%EC%9D%B4%EC%AE%B8%ED%8F%AC%EB%8F%84110G.jpg"
  }
  ]

    body = ""
    for i in json_data:
        body = body + json.dumps({"index": {"_index": "dictionary"}}) + '\n'
        body = body + json.dumps(i, ensure_ascii=False) + '\n'


    es.bulk(body)