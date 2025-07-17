from flask import Flask
from flask_cors import CORS
from .controllers.usuarios import usuarios_endpoints

def create_app():
    app = Flask(__name__)
    app.register_blueprint(usuarios_endpoints, url_prefix="/usuarios/api/v1")
    CORS(app, origins="*")
    return app
