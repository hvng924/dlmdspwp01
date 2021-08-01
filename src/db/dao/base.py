from sqlalchemy import engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from db.connection_factory import AbstractFactory
from ..connection_manager import get_connection

class Base:
    engine: Engine = None

    def __init__(self, connection_factory: AbstractFactory) -> None:
        self.engine = connection_factory.get_connection()

    def get_session() -> Session:
        Session = sessionmaker(bind=engine)
        return Session()