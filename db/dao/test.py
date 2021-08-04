from sqlalchemy.sql.expression import select
from db.connection_factory import AbstractFactory
from db.schemas.test import Test
from .base import BaseDAO

class TestDAO(BaseDAO):
    def __init__(self, connection_factory: AbstractFactory) -> None:
        super().__init__(connection_factory)

    def get_all(self):
        rows = []
        
        with self.get_session() as session:
            result = session.execute(select(Test))
            for row in result:
                rows.append({
                    'id': row.Test.id,
                    'x': row.Test.x,
                    'y': row.Test.y,
                })

        return rows

    def save(self, data):
        with self.get_session() as session:
            row = Test(x = data['x'], y = data['y'])
            session.add(row)
            session.commit()