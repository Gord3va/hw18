from flask import request, url_for
from flask_restx import Resource, Namespace
from dao.model.schemas import MovieSchema
from parsers import movie_parser
from setup_dao import movie_service

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """все фильмы, фильмы по режиссеру, жанру и году"""
        req = request.args
        if req:
            return movies_schema.dump(movie_service.get_by_request(req)), 200
        return movies_schema.dump(movie_service.get_all()), 200

    @movie_ns.expect(movie_parser)
    def post(self):
        """Добавляет"""
        movie = movie_service.create(movie_parser.parse_args())
        return movie_schema.dump(movie), 201, {'Location': f"{url_for('movies_movie_view', mid=movie.id)}"}


@movie_ns.route('/<int:mid>')
class MovieView(Resource):

    def get(self, mid: int):
        """фильм по его id"""
        return movie_schema.dump(movie_service.get_by_id(mid)), 200

    def put(self, mid: int):
        """Изменение"""
        req_json = request.json
        req_json['id'] = mid
        return movie_schema.dump(movie_service.update(req_json)), 204

    def delete(self, mid: int):
        """Удаляет"""
        movie_service.delete(mid)
        return "", 204
