from flask import jsonify, request, abort, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Resource, Namespace

import views

db = SQLAlchemy()

Products = Namespace(
    name="Products",
    description="Products 데이터를 조회하기 위해 사용하는 API.",
)

parser = Products.parser();
parser.add_argument('page', type=int, required=False, help='페이지번호')

# GET /api/products?page={page}
@Products.route('api/products')
@Products.expect(parser)
@Products.doc(responses={200: 'Success'})
@Products.doc(responses={404: 'We Can''t find Page'})
class ProductsClass(Resource):
    def get(self):
        """전체 상품 리스트를 페이지 별로 가져옵니다. """
        try:
            args = parser.parse_args()
            page = args['page']         # 쿼리스트링으로 받은 페이지
            if not 0 < int(page) <= 4:
                abort(404, "We Can't find Page")
            products, meta = views.get_product_all_list(page)
            return jsonify({
                'success': True,
                'data': products,
                'meta': meta
             })
        except TypeError:
            abort(404, "We Can't find Page")
