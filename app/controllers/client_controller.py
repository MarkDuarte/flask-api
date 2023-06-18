from models.client import Client
import uuid
from models import db

uuid_v4 = uuid.uuid4()

class ClientController:
    
    @staticmethod
    def list_client():
        clients = Client.query.all()
        result = []
        for client in clients:
            result.append({ 'id': uuid_v4, 'name': client.name, 'cnpj_cpf': client.cnpj_cpf, 'address': client.address})
        return result
    
    @staticmethod
    def create_client(name, cnpj_cpf, address):
        client = Client(name=name, cnpj_cpf=cnpj_cpf, address=address)
        db.session.add(client)
        db.session.commit()

    @staticmethod
    def update_client(id, name):
        client = Client.query.get(id)
        if client is None:
            return False
        client.name = name
        db.session.commit()
        return True
    
    @staticmethod
    def delete_client(id):
        client = Client.query.get(id)
        if client is None:
            return False
        db.session.delete(client)
        db.session.commit()
        return True