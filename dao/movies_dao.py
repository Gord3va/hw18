from __future__ import annotations

from dao.base_dao import BaseDAO
from dao.model.models import Movie


class MovieDAO(BaseDAO):

    def __init__(self, db_session):
        super().__init__(db_session, Movie)

    def get_by_director(self, director_id: int) -> list[Movie]:
        # Получить фильмы по id режиссера
        movies = self.session.query(Movie).filter(Movie.director_id == director_id).all()
        return movies

    def get_by_genre(self, genre_id: int) -> list[Movie]:
        # Получить фильмы по id жанра
        movies = self.session.query(Movie).filter(Movie.genre_id == genre_id).all()
        return movies

    def get_by_year(self, year: int) -> list[Movie]:
        # Получить фильмы по году
        movies = self.session.query(Movie).filter(Movie.year == year).all()
        return movies

    def create(self, data: dict) -> Movie:
        # Добавление нового фильма
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, movie: Movie) -> Movie | None:
        # Обновление фильма
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, movie: Movie):
        # Удаление фильма
        self.session.delete(movie)
        self.session.commit()
