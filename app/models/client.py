from . import db
import uuid

class Client(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    cnpj_cpf = db.Column(db.String(14), nullable=True)
    address = db.Column(db.String(200), nullable=True)

    def __init__(self, name, cnpj_cpf, address):
        self.id = str(uuid.uuid4())
        self.name = name
        self.cnpj_cpf = cnpj_cpf
        self.address = address
