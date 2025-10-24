from sqlmodel import Field, SQLModel


class ModelSpec:
    def __init__(self, model: SQLModel):
        self.model = model

    def table(self):
        return self.model.__tablename__
