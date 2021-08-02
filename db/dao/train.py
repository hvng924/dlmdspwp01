from sqlalchemy.sql.expression import select
from db.connection_factory import AbstractFactory
from db.dao.base import BaseDAO
from db.schemas.train import Train


class TrainDAO(BaseDAO):
    def __init__(self, connection_factory: AbstractFactory) -> None:
        super().__init__(connection_factory)

    def get_all(self):
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

    def save(self, data):
        with self.get_session() as session:
            row = Train(
                x = data['x'],
                y1 = data['y1'],
                y2 = data['y2'],
                y3 = data['y3'],
                y4 = data['y4'],
            )
            session.add(row)
            session.commit()