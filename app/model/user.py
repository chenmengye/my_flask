# @time: 2022-10-18 14:51
# @author: 39295
from sqlalchemy import Column, Integer, String
from app.model.base import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(24), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(128), nullable=False)