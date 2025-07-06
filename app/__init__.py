from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'

    # Import and register your routes here
    from app.routes.api import api_bp
    from app.routes.main import main_bp

    app.register_blueprint(api_bp)
    app.register_blueprint(main_bp)

    return app
