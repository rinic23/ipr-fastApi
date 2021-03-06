from sqlalchemy.orm import relationship
from core.db import Base
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import relationship
# СОЗДАЁМ МОДЕЛЬ ЮЗЕРОВ


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
