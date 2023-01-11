from flask import jsonify, request, abort, Blueprint
from flask_sqlalchemy import SQLAlchemy

import views

db = SQLAlchemy()
routes = Blueprint('products', __name__, url_prefix='/')

# GET /api/products?page={page}
@routes.route('/api/products', methods=['GET'])
def get_products():
    try:
        page = request.args.get('page', type=int, default=1)  # 쿼리스트링으로 받은 페이지
        if not 0 < int(page) <= 8:
            abort(404, "We Can't find Page")
        products, meta = views.get_product_all_list(page)
        return jsonify({
            'success': True,
            'data': products,
            'meta': meta
         })
    except TypeError:
        abort(404, "We Can't find Page")
