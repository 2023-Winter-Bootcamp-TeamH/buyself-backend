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
    try:
        if kw:
            products, meta = views.get_search(kw, page)
            return jsonify({
                'success': True,
                'data': products,
                'meta': meta
            })
    except :
        abort(500, "Something wrong in database")