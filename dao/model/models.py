# здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью (но не с базой)
#
# Пример
from setup_db import db


class BaseModel(db.Model):
    __abstract__ = True
    """Абстрактный класс - это класс в котором созданы абстрактные методы - методы, 
    которые обязательно должны присутствовать в дочерних классах. Создавть экзепмляр 
    абстрактного класса нельзя, его надо наследовать и уже у дочернего класса можно создать экземпляр.
     При этом экземпляр дочернего класса можно создать только в том случае, если у дочернего
      класса есть реализация всех абстрактных методов."""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class Movie(BaseModel):
    __tablename__ = "movie"
    title = db.Column(db.String(250))
    description = db.Column(db.Text)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    genre = db.relationship('Genre')
    director = db.relationship('Director')


class Director(BaseModel):
    __tablename__ = "director"
    name = db.Column(db.String(100))


class Genre(BaseModel):
    __tablename__ = "genre"
    name = db.Column(db.String(100))
