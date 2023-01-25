import requests
from flask import request, jsonify
from flask_restx import Namespace, Resource

from app import app

Products = Namespace(
    name="Products",
    description="Products 데이터를 조회하기 위해 사용하는 API.",
)
parser = Products.parser();
parser.add_argument('amount', type=int, required=False, help='총 금액')

@Products.route('api/payment')
@Products.expect(parser)
@Products.doc(responses={200: 'Success'})
@Products.doc(responses={404: 'We Can''t find Page'})
class Payment(Resource):
    def post(self):
        """카카오페이로 결제를 요청합니다. """
        args = parser.parse_args()
        amount = args['amount']
        URL = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            'Authorization': "KakaoAK " + "559e9369548a303adbea7e2555eb51c2",
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
        }
        params = {
            "cid": "TC0ONETIME",
            "partner_order_id": "1001",
            "partner_user_id": "testuser",
            "item_name": "BuySelf",
            "quantity": 1,
            "total_amount": amount,
            "tax_free_amount": 0,
            "vat_amount": 200,
            "approval_url": "http://localhost/api/payment/success",
            "cancel_url": "http://localhost/api/payment/cancel",
            "fail_url": "http://localhost/api/payment/fail"
        }

        res = requests.post(URL, headers=headers, params=params)
        app.tib = res.json()['tid']  # 결제 승인시 사용할 tid를 세션에 저장

        return jsonify({'next_url': res.json()['next_redirect_pc_url']})


def get_token():
    token = request.args.get("pg_token")

    return token


@Products.route('api/payment/success')
@Products.expect(parser)
@Products.doc(responses={200: 'Success'})
@Products.doc(responses={404: 'We Can''t find Page'})
class SuccessPayment(Resource):
    def get(self):
        """카카오페이 결제를 승인합니다. """
        pg_token = get_token()
        URL = 'https://kapi.kakao.com/v1/payment/approve'
        headers = {
            "Authorization": "KakaoAK " + "559e9369548a303adbea7e2555eb51c2",
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
        }
        params = {
            "cid": "TC0ONETIME",  # 테스트용 코드
            "tid": app.tib,  # 결제 요청시 세션에 저장한 tid
            "partner_order_id": "1001",  # 주문번호
            "partner_user_id": "testuser",  # 유저 아이디
            "pg_token": pg_token,  # 쿼리 스트링으로 받은 pg토큰
        }

        requests.post(URL, headers=headers, params=params)

        return True

@Products.route('api/payment/cancel')
@Products.expect(parser)
@Products.doc(responses={200: 'Success'})
@Products.doc(responses={404: 'We Can''t find Page'})
class CanclePayment(Resource):
    def get(self):
        """카카오페이 결제를 취소합니다. """
        URL = "https://kapi.kakao.com/v1/payment/order"
        headers = {
            "Authorization": "KakaoAK " + "559e9369548a303adbea7e2555eb51c2",
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
        }
        params = {
            "cid": "TC0ONETIME",  # 가맹점 코드
            "tid": app.tib,  # 결제 고유 코드

        }

        requests.post(URL, headers=headers, params=params)

        return False

@Products.route('api/payment/fail')
@Products.expect(parser)
@Products.doc(responses={200: 'Success'})
@Products.doc(responses={404: 'We Can''t find Page'})
class FailPayment(Resource):
    def get(self):
        """결제 버튼 클릭 후 15분이 지나도 결제가 안되면 결제 실패합니다. """
        return False