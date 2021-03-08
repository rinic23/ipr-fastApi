from .shemas import UserCreate
from sqlalchemy.orm import Session
from .models import User


def get_user_list(db: Session):
    return db.query(User).all()


def create_user_service(data: UserCreate, db: Session):
    user = User(**data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_id_service(db: Session, id: int):
    user = db.query(User).get(id)
    user.posts
    return user


def update_user_by_id_service(post_data: UserCreate, db: Session, id: int):
    user = db.query(User).get(id)
    for key, value in post_data:
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user
