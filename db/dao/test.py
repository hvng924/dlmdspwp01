from sqlalchemy.sql.expression import select
from db.connection_factory import AbstractFactory
from db.schemas.test import Test
from .base import BaseDAO


class TestDAO(BaseDAO):
    def __init__(self, connection_factory: AbstractFactory) -> None:
        super().__init__(connection_factory)

    def get_all(self) -> list:
        """Get all rows

        Returns:
            list: list of dict of data in table
        """
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

    def save(self, data: dict):
        """Insert data

        Args:
            data (dict): data values
        """
        with self.get_session() as session:
            row = Test()
            for key in data.keys():
                setattr(row, key, data[key])
            session.add(row)
            session.commit()