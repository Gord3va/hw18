# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
from flask_restx import Resource, Namespace
from dao.model.schemas import GenreSchema
from setup_dao import genre_service

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):

    def get(self):
        """все жанры"""
        return genres_schema.dump(genre_service.get_all()), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):

    def get(self, gid: int):
        """жанр по его id"""

        if genre_service.get_by_id(gid) is None:
            return "", 404
        return genre_schema.dump(genre_service.get_by_id(gid)), 200
