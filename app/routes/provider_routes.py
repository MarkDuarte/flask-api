from flask import Blueprint, jsonify, request
from controllers.provider_controller import ProviderController

provider_routes = Blueprint('provider_routes', __name__)

@provider_routes.route('/fornecedores', methods=['GET'])
def listar_fornecedores():
    fornecedores = ProviderController.list_provider()
    return jsonify(fornecedores)

@provider_routes.route('/fornecedores', methods=['POST'])
def criar_fornecedor():
    name = request.json['name']
    price = request.json['price']
    ProviderController.create_provider(name, price)
    return jsonify({'mensagem': 'Fornecedor criado com sucesso!'})

@provider_routes.route('/fornecedores/<string:id>', methods=['PUT'])
def atualizar_fornecedor(id):
    name = request.json['name']
    if ProviderController.update_provider(id, name):
        return jsonify({'mensagem': 'Fornecedor atualizado com sucesso!'})
    return jsonify({'mensagem': 'Fornecedor não encontrado'}), 404

@provider_routes.route('/fornecedores/<string:id>', methods=['DELETE'])
def excluir_fornecedor(id):
    if ProviderController.delete_provider(id):
        return jsonify({'mensagem': 'Fornecedor excluído com sucesso!'})
    return jsonify({'mensagem': 'Fornecedor não encontrado'}), 404
