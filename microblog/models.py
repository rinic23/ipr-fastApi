from datetime import time
from sqlalchemy.sql.expression import true
from core.db import Base
from sqlalchemy import Column, String, Integer, DateTime

# СОЗДАЁМ МОДЕЛЬ ПОСТОВ


class Post(Base):
    __tablename__ = 'microblog_posts'

    id = Column(Integer, primary_key=true, index=true, unique=True)
    title = Column(String)
    text = Column(String)
    Date = Column(DateTime)
