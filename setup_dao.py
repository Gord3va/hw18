# Создание DAO и сервисов
from dao.base_dao import BaseDAO
from dao.model.models import Genre, Director
from dao.movies_dao import MovieDAO
from service.base_service import BaseService

from service.movie_service import MovieService
from setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

director_dao = BaseDAO(db.session, Director)
director_service = BaseService(director_dao)

genre_dao = BaseDAO(db.session, Genre)
genre_service = BaseService(genre_dao)
