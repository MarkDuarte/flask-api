from flask import jsonify, request
from controllers.purchase_controller import PurchaseController

class PurchaseRoutes:
    @staticmethod
    def list_purchase():
        purchases = PurchaseController.list_purchase()
        return jsonify(purchases)

    @staticmethod
    def create_purchase():
        name = request.json['name']
        PurchaseController.create_purchase(name)
        return jsonify({'mensagem': 'Compra criado com sucesso!'})
