from flask import jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Resource, Namespace

import views

db = SQLAlchemy()

Products = Namespace(
    name="Products",
    description="Prodeucts 데이터를 조회하기 위해 사용되는 API.",
)

parser = Products.parser()
parser.add_argument('kw', type=str, required=False, help='검색어 입력')

# GET /api/search?kw={kw}
@Products.route('api/search')
@Products.expect(parser)
@Products.doc(responses={200: 'Success'})
@Products.doc(responses={500: 'We Can''t find data'})
class ProductsClass(Resource):
    def get(self):
        """키워드 검색을 통해 상품 정보를 가져옵니다. """
        page = request.args.get('page', type=int, default=1)
        args = parser.parse_args()
        kw = args['kw']
        products, meta = views.get_search(kw, page)
        return jsonify({
            'success': True,
            'data': products,
            'meta': meta
        })