from flask import Blueprint

routes = Blueprint('main', __name__, url_prefix='/')

@routes.route('/')
def hello_pybo():
    return 'Main Views!'