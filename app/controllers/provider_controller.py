from models import db
from models.provider import Provider

class ProviderController:
    @staticmethod
    def list_provider():
        providers = Provider.query.all()
        result = []
        for provider in providers:
            result.append({'id': provider.id, 'name': provider.name, 'price': provider.price})
        return result
    
    @staticmethod
    def create_provider(name, price):
        provider = Provider(name=name, price=price)
        db.session.add(provider)
        db.session.commit()

    @staticmethod
    def update_provider(id, name):
        provider = Provider.query.get(id)
        if provider is None:
            return False
        provider.name = name
        db.session.commit()
        return True
    
    @staticmethod
    def delete_provider(id):
        provider = Provider.query.get(id)
        if provider is None:
            return False
        db.session.delete(provider)
        db.session.commit()
        return True
