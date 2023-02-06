from flask_restx import Resource, Namespace
from dao.model.schemas import DirectorSchema
from setup_dao import director_service

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        """всех режиссеров"""
        return directors_schema.dump(director_service.get_all()), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):

    def get(self, did: int):
        """режиссера по его id"""
        return director_schema.dump(director_service.get_by_id(did)), 200
