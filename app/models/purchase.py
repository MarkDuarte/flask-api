import uuid
from models import db

class Purchase(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    product_id = db.Column(db.String(36), db.ForeignKey('product.id'), nullable=False)
    client_id = db.Column(db.String(36), db.ForeignKey('client.id'), nullable=False)

    def __init__(self, product_id, client_id):
        self.id = str(uuid.uuid4())
        self.product_id = product_id
        self.client_id = client_id