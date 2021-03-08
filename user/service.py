from .shemas import UserCreate, UserList
from sqlalchemy.orm import Session, aliased
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


def get_user_by_id_service(db: Session, id: int):
    user = db.query(User).get(id)
    user.posts
    return user

  # user_alias = aliased(User, name='EGOR')
    # q = db.query(User).filter(User.name == 'EGOR')
    # user_post_list = db.query(User, User.name, user_alias)
    # print(q, 'шооооо')
    # print(user_post_list.column_descriptions)
    # some_user = db.query(User).filter_by(name='EGOR').first()
    # some_user = db.query(User).all()
    # print(some_user.children)
    # print(dict(some_user))
