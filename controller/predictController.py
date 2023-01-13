from flask import Blueprint, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from controller.imageController import *
import views
import tasks

db = SQLAlchemy()
routes = Blueprint('predict', __name__)

@routes.route('/api/predict', methods=['POST'])
def test():
    if request.method == 'POST':
        file = request.files["file"]
        img_name = post_image(file)
        get_url(img_name)
        use_url(img_name)
        task = tasks.prediction.delay(img_name)
        result = []
        for i in task.get():
            product = views.get_products_id_list(int(i['id']))
            result.append({'class_name': product['class_name'], 'price': product['price'], 'img_url': product['img_url']})

        return jsonify(result)