from sqlalchemy.sql.expression import select
from db.schemas.ideal import Ideal
from db.connection_factory import AbstractFactory
from db.dao.base import BaseDAO


class IdealDAO(BaseDAO):
    def __init__(self, connection_factory: AbstractFactory) -> None:
        super().__init__(connection_factory)

    def get_all(self):
        rows = []

        with self.get_session() as session:
            result = session.execute(select(Ideal))

            for row in result:
                rows.append({
                    'id': row.Ideal.id,
                    'x': row.Ideal.x,
                    'y1': row.Ideal.y1,
                    'y2': row.Ideal.y2,
                    'y3': row.Ideal.y3,
                    'y4': row.Ideal.y4,
                    'y5': row.Ideal.y5,
                    'y6': row.Ideal.y6,
                    'y7': row.Ideal.y7,
                    'y8': row.Ideal.y8,
                    'y9': row.Ideal.y9,
                    'y10': row.Ideal.y10,
                    'y11': row.Ideal.y11,
                    'y12': row.Ideal.y12,
                    'y13': row.Ideal.y13,
                    'y14': row.Ideal.y14,
                    'y15': row.Ideal.y15,
                    'y16': row.Ideal.y16,
                    'y17': row.Ideal.y17,
                    'y18': row.Ideal.y18,
                    'y19': row.Ideal.y19,
                    'y20': row.Ideal.y20,
                    'y21': row.Ideal.y21,
                    'y22': row.Ideal.y22,
                    'y23': row.Ideal.y23,
                    'y24': row.Ideal.y24,
                    'y25': row.Ideal.y25,
                    'y26': row.Ideal.y26,
                    'y27': row.Ideal.y27,
                    'y28': row.Ideal.y28,
                    'y29': row.Ideal.y29,
                    'y30': row.Ideal.y30,
                    'y31': row.Ideal.y31,
                    'y32': row.Ideal.y32,
                    'y33': row.Ideal.y33,
                    'y34': row.Ideal.y34,
                    'y35': row.Ideal.y35,
                    'y36': row.Ideal.y36,
                    'y37': row.Ideal.y37,
                    'y38': row.Ideal.y38,
                    'y39': row.Ideal.y39,
                    'y40': row.Ideal.y40,
                    'y41': row.Ideal.y41,
                    'y42': row.Ideal.y42,
                    'y43': row.Ideal.y43,
                    'y44': row.Ideal.y44,
                    'y45': row.Ideal.y45,
                    'y46': row.Ideal.y46,
                    'y47': row.Ideal.y47,
                    'y48': row.Ideal.y48,
                    'y49': row.Ideal.y49,
                    'y50': row.Ideal.y50,
                })
        
        return rows

    def save(self, data):
        with self.get_session() as session:
            row = Ideal()
            for key in data.keys():
                setattr(row, key, data[key])
            session.add(row)
            session.commit()