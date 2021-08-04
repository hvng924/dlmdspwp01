from sqlalchemy import engine
from sqlalchemy.engine import base
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from db.connection_factory import AbstractFactory
import db.schemas.base as sb


"""
Base class of all DAO classes
"""
class BaseDAO:
    conn: Engine = None

    """
    Establish connection and create all tables
    
    :param connection_factory: AbtractFactory -- A connection factory class
    :returns: None
    """
    def __init__(self, connection_factory: AbstractFactory) -> None:
        self.conn = connection_factory.get_connection()
        sb.Base.metadata.create_all(self.conn)

    """
    Get session object from current `engine`

    :returns: Session object
    """
    def get_session(self) -> Session:
        Session = sessionmaker(bind=self.conn)
        return Session()