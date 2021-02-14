from datetime import time
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.schema import ForeignKey
from core.db import Base
from sqlalchemy import Column, String, Integer, DateTime
# СОЗДАЁМ МОДЕЛЬ ПОСТОВ


class Post(Base):
    __tablename__ = 'microblog_posts'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String)
    Date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='microblog_posts')
