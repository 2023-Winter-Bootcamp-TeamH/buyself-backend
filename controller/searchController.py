from flask import jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Resource, Namespace
from elasticsearch import Elasticsearch


from controller.elasticSearch import inputData

es = Elasticsearch("http://elastic:9200/")

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
        inputData()
        args = parser.parse_args()
        kw = args['kw']
        if not kw:
            return Response(status=404)
        product_results = es.search(index='dictionary', body={'query': {'match': {'class_name': str(kw)}}})
        data_list = []
        for product_result in product_results['hits']['hits']:
            data_list.append(product_result['_source'])
        meta = {
            "page": 1,
            "pages": 4,
            "total_count": 22,
            "prev_page": None,
            "next_page": 2,
            "has_next": True,
            "has_prev": False
        }
        result = jsonify({
            'success': True,
            'data': data_list,
            'meta': meta
        })
        return result
