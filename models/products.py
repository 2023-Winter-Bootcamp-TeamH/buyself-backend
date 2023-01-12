from app import db
from datetime import datetime

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
