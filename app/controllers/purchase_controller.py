from models.purchase import Purchase
import uuid
from models import db

uuid_v4 = uuid.uuid4()

class PurchaseController:
    
    @staticmethod
    def list_purchase():
        purchases = Purchase.query.all()
        result = []
        for purchase in purchases:
            result.append({ 'id': uuid_v4, 'name': purchase.name})
        return result
    
    @staticmethod
    def create_purchase(product_id, client_id):
        purchase = Purchase(product_id=product_id, client_id=client_id)
        db.session.add(purchase)
        db.session.commit()