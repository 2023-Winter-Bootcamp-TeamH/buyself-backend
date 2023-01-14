from flask import Blueprint, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from controller.imageController import *
import views
import tasks

db = SQLAlchemy()
routes = Blueprint('predict', __name__)


@routes.route('/api/predict', methods=['POST'])
def detect_object():
    if request.method == 'POST':
        try:
            image = request.files["file"]
            img_name = post_image(image)
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
            abort(500, "Wrong")
