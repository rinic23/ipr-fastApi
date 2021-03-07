from .shemas import UserCreate, UserList
from sqlalchemy.orm import Session
from .models import User


def get_user_list(db: Session):
    return db.query(User).all()


def create_user_service(data: UserCreate, db: Session):
    user = User(**data.dict())
    db.add(user)
    print(data)
    db.commit()
    db.refresh(user)
    return user
