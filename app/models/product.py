import uuid
from models import db

class Product(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float)
    provider_id = db.Column(db.String(36), db.ForeignKey('provider.id'), nullable=False)

    def __init__(self, name, price, provider_id):
        self.id = str(uuid.uuid4())
        self.name = name
        self.price = price
        self.provider_id = provider_id

