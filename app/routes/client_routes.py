from flask import Blueprint, jsonify, request
from controllers.client_controller import ClientController

client_routes = Blueprint('client_routes', __name__)

@client_routes.route('/clientes', methods=['GET'])
def list_client():
    clients = ClientController.list_client()
    return jsonify(clients)

@client_routes.route('/clientes', methods=['POST'])
def create_client():
    name = request.json['name']
    cnpj_cpf = request.json['cnpj_cpf']
    address = request.json['address']
    ClientController.create_client(name, cnpj_cpf, address)
    return jsonify({'mensagem': 'Cliente cadastrado com sucesso!'})

@client_routes.route('/clientes/<string:id>', methods=['PUT'])
def update_client(id):
    name = request.json['name']
    if ClientController.update_client(id, name):
        return jsonify({'mensagem': 'Cliente atualizado com sucesso!'})
    return jsonify({'mensagem': 'Cliente não encontrado'}), 404

@client_routes.route('/clientes/<string:id>', methods=['DELETE'])
def delete_client(id):
    if ClientController.delete_client(id):
        return jsonify({'mensagem': 'Cliente excluído com sucesso!'})
    return jsonify({'mensagem': 'Cliente não encontrado'}), 404
