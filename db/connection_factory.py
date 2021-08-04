from sqlalchemy import engine
from sqlalchemy.engine.base import Engine


class AbstractFactory:
    @staticmethod
    def get_connection() -> Engine:
        """Get connection engine

        Raises:
            NotImplemented: no implementation error

        Returns:
            Engine: connection engine
        """
        raise NotImplemented


SQLITE_MEM_ENGINE = None
class SqliteMemoryFactory(AbstractFactory):
    @staticmethod
    def get_connection() -> Engine:
        global SQLITE_MEM_ENGINE
        
        if SQLITE_MEM_ENGINE is None:
            SQLITE_MEM_ENGINE = engine.create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
        return SQLITE_MEM_ENGINE


SQLITE_ENGINE = None
class SqliteFactory(AbstractFactory):
    @staticmethod
    def get_connection() -> Engine:
        global SQLITE_ENGINE
        
        if SQLITE_ENGINE is None:
            SQLITE_ENGINE = engine.create_engine("sqlite:///data.db", echo=True, future=True)
        return SQLITE_ENGINE
