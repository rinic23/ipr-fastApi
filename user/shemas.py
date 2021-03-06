from typing import List
from pydantic import BaseModel
from microblog.shemas import PostList

# БАЗОВЫЙ КЛАСС ПОСТОВ


class UserBase(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True

# БАЗОВЫЙ КЛАСС ПОЛУЧЕНИЯ СПИСКА ПОСТОВ


class UserList (UserBase):
    id: int
    posts: List[PostList]

# КЛАСС СОЗДАНИЯ ПОСТОВ


class UserCreate(UserBase):
    pass
