from models.products import Products


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

# 검색api, kw: 검색어
def get_search(kw, page):
    products = []
    search = '%%{}%%'.format(kw)
    pagination = Products.query.filter(Products.class_name.ilike(search)).paginate(page=page,per_page=3 ,error_out=False)
    for p in pagination.items:
        product = {'class_name': p.class_name,
                 'price': p.price,
                 'img_url': p.img_url}
        products.append(product)
    meta = get_page_list(pagination)
    return products, meta