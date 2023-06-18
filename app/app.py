from flask import Flask
from routes.provider_routes import provider_routes
from routes.product_routes import product_routes
from routes.client_routes import client_routes
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

with app.app_context():
    db.create_all()  # Cria as tabelas no banco de dados

# Registrar o blueprint no aplicativo Flask
app.register_blueprint(provider_routes, url_prefix='/')
app.register_blueprint(product_routes, url_prefix='/')
app.register_blueprint(client_routes, url_prefix='/')


if __name__ == '__main__':
    app.run(debug=True)
