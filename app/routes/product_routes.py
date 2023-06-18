from flask import Blueprint, jsonify, request
from controllers.product_controller import ProductController

product_routes = Blueprint('product_routes', __name__)

@product_routes.route('/produtos', methods=['GET'])
def listar_produtos():
    produtos = ProductController.list_product()
    return jsonify(produtos)

@product_routes.route('/produtos', methods=['POST'])
def criar_produto():
    name = request.json['name']
    price = request.json['price']
    provider_id = request.json['provider_id']
    ProductController.create_product(name, price, provider_id)
    return jsonify({'mensagem': 'Produto cadastrado com sucesso!'})

@product_routes.route('/produtos/<string:id>', methods=['PUT'])
def atualizar_produto(id):
    name = request.json['name']
    price = request.json['price']
    if ProductController.update_product(id, name, price):
        return jsonify({'mensagem': 'Produto atualizado com sucesso!'})
    return jsonify({'mensagem': 'Produto não encontrado'}), 404

@product_routes.route('/produto/<string:id>', methods=['DELETE'])
def excluir_produto(id):
    if ProductController.delete_product(id):
        return jsonify({'mensagem': 'Produto excluído com sucesso!'})
    return jsonify({'mensagem': 'Produto não encontrado'}), 404
