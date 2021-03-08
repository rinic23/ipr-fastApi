from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.schema import ForeignKey
from core.db import Base
from sqlalchemy import Column, String, Integer, DateTime
from user.models import User
# СОЗДАЁМ МОДЕЛЬ ПОСТОВ


class Post(Base):
    __tablename__ = 'microblog_posts'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String)
    Date = Column(DateTime)
    user = Column(Integer, ForeignKey('user.id'))
