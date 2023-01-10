from flask import jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from . import routes
from .. import views

db = SQLAlchemy()

# GET /api/products?page={page}
@routes.route('/api/products/<int:page>', methods=['GET'])
def get_products(page):
    page = request.args.get('page', type=int, default=1)  # 쿼리스트링으로 받은 페이지
    try:
        products, meta = views.get_product_all_list(page)
        return jsonify({
            'success': True,
            'data': products,
            'meta': meta
        })
    except Exception as e:
        print('예외가 발생했습니다.', e)