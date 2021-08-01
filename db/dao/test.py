from sqlalchemy.sql.expression import select
from db.connection_factory import AbstractFactory
from db.schemas.test import Test
from .base import Base

class TestDAO(Base):
    def __init__(self, connection_factory: AbstractFactory) -> None:
        super().__init__(connection_factory)

    def get_all(self):
        rows = []
        
        with self.get_session() as session:
            result = session.execute(select(Test))
            for row in result:
                rows.append({
                    'x': row.Test.x,
                    'y': row.Test.y,
                })

        return rows

    def save(self, entry):
        with self.get_session() as session:
            row = Test(x = entry['x'], y = entry['y'])
            session.add(row)
            session.commit()