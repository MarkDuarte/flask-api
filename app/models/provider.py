import uuid
from models import db

class Provider(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Float)

    def __init__(self, name, price):
        self.id = str(uuid.uuid4())
        self.name = name
        self.price = price

