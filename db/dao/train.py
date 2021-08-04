from sqlalchemy.sql.expression import select
from db.connection_factory import AbstractFactory
from db.dao.base import BaseDAO
from db.schemas.train import Train


class TrainDAO(BaseDAO):
    def __init__(self, connection_factory: AbstractFactory) -> None:
        super().__init__(connection_factory)

    def get_all(self) -> list:
        """Get all rows

        Returns:
            list: list of dict of data in table
        """
        rows = []

        with self.get_session() as session:
            result = session.execute(select(Train))

            for row in result:
                rows.append({
                    'id': row.Train.id,
                    'x': row.Train.x,
                    'y1': row.Train.y1,
                    'y2': row.Train.y2,
                    'y3': row.Train.y3,
                    'y4': row.Train.y4,
                })
        
        return rows

    def save(self, data: dict):
        """Insert data

        Args:
            data (dict): data values
        """
        with self.get_session() as session:
            row = Train()
            for key in data.keys():
                setattr(row, key, data[key])
            session.add(row)
            session.commit()