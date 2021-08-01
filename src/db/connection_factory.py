from sqlalchemy import engine
from sqlalchemy.engine.base import Engine


class AbstractFactory:
    @staticmethod
    def get_connection() -> Engine:
        raise NotImplemented

SQLITE_ENGINE = None
class SqliteFactory(AbstractFactory):
    @staticmethod
    def get_connection() -> Engine:
        if SQLITE_ENGINE is None:
            SQLITE_ENGINE = engine.create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
        return SQLITE_ENGINE
