from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

ENGINE = None

def get_connection() -> Engine:
    if ENGINE is None:
        ENGINE = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
    return ENGINE