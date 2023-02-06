# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для
# приложения. этот файл часто является точкой входа в приложение

from typing import Type

from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.movies import movie_ns
from views.directors import director_ns
from views.genres import genre_ns


def create_app(config_object: Type[Config]) -> Flask:
    #создание основного объекта app
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.url_map.strict_slashes = False
    app.app_context().push()
    register_extensions(app)
    return app


def register_extensions(app: Flask) -> Api:
    #подключение расширений
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


app = create_app(Config)

if __name__ == '__main__':
    app.run(host="localhost", port=10001)
