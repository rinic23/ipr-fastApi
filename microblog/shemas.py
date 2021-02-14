from pydantic import BaseModel
from datetime import datetime

# БАЗОВЫЙ КЛАСС ПОСТОВ


class PostBase(BaseModel):
    title: str
    text: str
    Date: datetime

    class Config:
        orm_mode = True

# БАЗОВЫЙ КЛАСС ПОЛУЧЕНИЯ СПИСКА ПОСТОВ


class PostList (PostBase):
    id: int

# КЛАСС СОЗДАНИЯ ПОСТОВ
class PostCreate(PostBase):
    pass
