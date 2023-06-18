from flask import Blueprint, jsonify, request
from controllers.purchase_controller import PurchaseController

purchase_routes = Blueprint('purchase_routes', __name__)

@purchase_routes.route('/compras', methods=['GET'])
def list_purchase():
    compras = PurchaseController.list_purchase()
    return jsonify(compras)

@purchase_routes.route('/compras', methods=['POST'])
def create_purchase():
    client_id = request.json['client_id']
    product_id = request.json['product_id']
    PurchaseController.create_provider(product_id, client_id)
    return jsonify({'mensagem': 'Compra efetuado com sucesso!'})
