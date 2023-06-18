from . import db

class Purchase(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    product_id = db.Column(db.String(36), db.ForeignKey('product.id'), nullable=False)
    client_id = db.Column(db.String(36), db.ForeignKey('client.id'), nullable=False)