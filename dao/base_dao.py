from flask_sqlalchemy.model import Model


class BaseDAO:

    def __init__(self, session, model):
        self.session = session
        self.model = model

    def get_all(self) -> list[Model]:
        # Получить все
        return self.session.query(self.model).all()

    def get_by_id(self, gid: int) -> Model:
        # Получить по id
        return self.session.query(self.model).get(gid)
