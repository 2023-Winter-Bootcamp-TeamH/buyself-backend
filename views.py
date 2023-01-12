from models.products import *
from app import db

def get_products_id_list(products_id):
    p = db.session.query(Products).filter(Products.id == products_id).first()
    product = {'id': p.id,
               'class_name': p.class_name,
               'price': p.price,
               'img_url': p.img_url}

    return product