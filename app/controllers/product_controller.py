from models import db
from models.product import Product
import uuid

uuid_v4 = uuid.uuid4()

class ProductController:
    
    @staticmethod
    def list_product():
        products = Product.query.all()
        result = []
        for product in products:
            result.append({ 'id': uuid_v4, 'name': product.name, 'price': product.price, 'provider_id': product.provider_id })
        return result
    
    @staticmethod
    def create_product(name, price, provider_id):
        product = Product(name=name, price=price, provider_id=provider_id)
        db.session.add(product)
        db.session.commit()

    @staticmethod
    def update_product(id, name, price):
        product = Product.query.get(id)
        if product is None:
            return False
        product.name = name
        product.price = price
        db.session.commit()
        return True
    
    @staticmethod
    def delete_product(id):
        product = Product.query.get(id)
        if product is None:
            return False
        db.session.delete(product)
        db.session.commit()
        return True