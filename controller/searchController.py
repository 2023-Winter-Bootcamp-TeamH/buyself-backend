from flask import jsonify, request, abort, Blueprint
from flask_sqlalchemy import SQLAlchemy

import views

db = SQLAlchemy()
routes = Blueprint('search', __name__, url_prefix='/')

# GET /search?kw={kw}
@routes.route('/search', methods=['GET'])
def get_search():
    kw = request.args.get('kw', type=str, default='')  # 검색어
    page = request.args.get('page', type=int, default=1)
    products, meta = views.get_search(kw, page)
    print(products)
    try:
        if kw == '':
            return "검색어를 입력해주세요."
        elif products == []:
            return "해당 상품이 없습니다."
        else:
            return jsonify({
                'success': True,
                'data': products,
                'meta': meta
            })
    except :
        abort(500, "검색어를 입력해주세요")