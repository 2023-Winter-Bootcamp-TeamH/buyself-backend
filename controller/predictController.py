from flask import Blueprint, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from controller.imageController import *
from flask_restx import Resource, Namespace
from werkzeug.datastructures import FileStorage
import views
import tasks

db = SQLAlchemy()

Products = Namespace(
    name="Products",
    description="Products 데이터를 조회하기 위해 사용하는 API.",
)

upload_parser = Products.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=False)

@Products.route('api/predict/')
@Products.expect(upload_parser)
@Products.doc(responses={200: 'Success'})
@Products.doc(responses={500: 'Wrong request'})
class Predict_Object(Resource):
    def post(self):
        """사용자가 계산한 상품을 인식해 화면에 띄웁니다 """
        if request.method == 'POST':
            try:
                args = upload_parser.parse_args()
                file = args.get("file")
                img_name = post_image(file)
                url = get_url(img_name)
                task = tasks.prediction.delay(url)

                result = []
                for i in task.get():
                    product = views.get_products_id_list(int(i['id']))
                    result.append(
                        {'class_name': product['class_name'], 'price': product['price'], 'img_url': product['img_url']})

                delete_image(img_name)

                return jsonify(result)
            except:
                abort(500, "We can't find any object")
