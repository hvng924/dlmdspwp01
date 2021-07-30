from sqlalchemy import *
from sqlalchemy.sql.elements import True_
from sqlalchemy.sql.functions import session_user
from .base import Base

class Test(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True, autoincrement=True) # Required for SQLAlchemy Mapping
    x = Column(Float)
    y = Column(Float)