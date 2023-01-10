from flask import Blueprint

from . import routes

@routes.route('/')
def hello_pybo():
    return 'Main Views!'