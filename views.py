from app import db
from models.products import Products

# DB에 있는 products id 리스트 받아오기
def get_products_id_list(products_id):
    p = db.session.query(Products).filter(Products.id == products_id).first()
    product = {'id': p.id,
               'class_name': p.class_name,
               'price': p.price,
               'img_url': p.img_url}
    return product

# 전체 상품 리스트 반환
def get_product_all_list(page):
    products = []
    pagination = Products.query.paginate(page=page, per_page=6, error_out=False)
    for p in pagination.items:
        product = {'id': p.id,
                 'class_name': p.class_name,
                 'price': p.price,
                 'img_url': p.img_url}
        products.append(product)
    meta = get_page_list(pagination)
    return products, meta

# 페이지 정보 반환
def get_page_list(pagination):
    meta = {
        "page": pagination.page,
        "pages": pagination.pages,
        "total_count": pagination.total,
        "prev_page": pagination.prev_num,
        "next_page": pagination.next_num,
        "has_next": pagination.has_next,
        "has_prev": pagination.has_prev
    }
    return meta