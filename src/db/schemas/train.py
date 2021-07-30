from typing import Tuple
from sqlalchemy import *
from sqlalchemy.sql.elements import True_
from sqlalchemy.sql.functions import session_user
from .base import Base

class Train(Base):
    __tablename__ = 'train'

    id = Column(Integer, primary_key=True, autoincrement=True) # Required for SQLAlchemy Mapping
    x = Column(Float)
    y1 = Column(Float)
    y2 = Column(Float)
    y3 = Column(Float)
    y4 = Column(Float)