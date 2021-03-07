from pydantic import BaseModel


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

# КЛАСС СОЗДАНИЯ ПОСТОВ


class UserCreate(UserBase):
    pass
