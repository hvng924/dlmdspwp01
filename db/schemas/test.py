from db.connection_factory import SqliteMemoryFactory
from sqlalchemy import *
from sqlalchemy.sql.elements import True_
from sqlalchemy.sql.functions import session_user
from .base import Base

class Test(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True, autoincrement=True) # Required for SQLAlchemy Mapping
    x = Column(Float)
    y = Column(Float)


class TestIdeal(Base):
    __tablename__ = 'test_ideal'

    id = Column(Integer, primary_key=True, autoincrement=True) # Required for SQLAlchemy Mapping
    x = Column(Float)
    y = Column(Float)
    delta_y = Column(Float)
    ideal_no = Column(Integer)