# this is the "web_app/__init__.py" file...
import os

from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.search_routes import search_routes
from web_app.routes.class_routes import class_routes


SECRET_KEY = os.getenv("SECRET_KEY", default="super secret")

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY

    app.register_blueprint(home_routes)
    app.register_blueprint(search_routes)
    app.register_blueprint(class_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)