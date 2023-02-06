from __future__ import annotations

from dao.model.models import Movie
from service.base_service import BaseService


class MovieService(BaseService):

    def get_by_request(self, data: dict) -> list[Movie] | None:
        # Получить фильмы по id режиссера, id жанра и году
        if "director_id" in data:
            movies = self.dao.get_by_director(data.get('director_id'))
            return movies
        if "genre_id" in data:
            movies = self.dao.get_by_genre(data.get('genre_id'))
            return movies
        if "year" in data:
            movies = self.dao.get_by_year(data.get('year'))
            return movies
        return None

    def create(self, data: dict) -> Movie:
        # Добавление
        return self.dao.create(data)

    def update(self, data: dict) -> Movie | None:
        # Обновление
        try:
            mid = data.get('id')
            movie = self.dao.get_by_id(mid)
            movie.title = data.get('title')
            movie.description = data.get('description')
            movie.trailer = data.get('trailer')
            movie.year = data.get('year')
            movie.rating = data.get('rating')
            movie.genre_id = data.get('genre_id')
            movie.director_id = data.get('director_id')
            return self.dao.update(movie)
        except Exception:
            return None

    def delete(self, mid: int) -> Movie | None:
        # Удаление
        movie = self.dao.get_by_id(mid)
        return self.dao.delete(movie)