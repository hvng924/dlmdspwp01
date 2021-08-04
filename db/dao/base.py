from sqlalchemy import engine
from sqlalchemy.engine import base
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from db.connection_factory import AbstractFactory
import db.schemas.base as sb


class BaseDAO:
    conn: Engine = None
    
    def __init__(self, connection_factory: AbstractFactory) -> None:
        """Establish connection and create all DB tables

        Args:
            connection_factory (AbstractFactory): Database connection factory class
        """
        self.conn = connection_factory.get_connection()
        sb.Base.metadata.create_all(self.conn)

    def get_session(self) -> Session:
        """Get session object from current connection engine

        Returns:
            Session: session object
        """
        Session = sessionmaker(bind=self.conn)
        return Session()