from flask import jsonify, request
from controllers.client_controller import ClientController

class ClientRoutes:
    @staticmethod
    def list_client():
        clients = ClientController.list_client()
        return jsonify(clients)

    @staticmethod
    def create_product():
        name = request.json['name']
        ClientController.create_client(name)
        return jsonify({'mensagem': 'Produto criado com sucesso!'})

    @staticmethod
    def update_client(id):
        name = request.json['name']
        if ClientController.update_client(id, name):
            return jsonify({'mensagem': 'Produto atualizado com sucesso!'})
        return jsonify({'mensagem': 'Produto não encontrado'}), 404

    @staticmethod
    def delete_client(id):
        if ClientController.delete_client(id):
            return jsonify({'mensagem': 'Produto excluído com sucesso!'})
        return jsonify({'mensagem': 'Produto não encontrado'}), 404
