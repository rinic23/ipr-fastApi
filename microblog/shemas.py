from pydantic import BaseModel
from datetime import datetime

# БАЗОВЫЙ КЛАСС ПОСТОВ


class PostBase(BaseModel):
    title: str
    text: str

# БАЗОВЫЙ КЛАСС ПОЛЬЗОВАТЕЛЕЙ


class PostList (PostBase):
    date: datetime
    id: int

    class Config:
        orm_mode = True
