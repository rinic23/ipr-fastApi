# ЛОГИКА ОБЩЕНИЯ С БД
from sqlalchemy.orm import Session
from .models import Post
from .shemas import PostCreate

# ФУНКЦИЯ КОТОРАЯ ПОЛУЧЕТ ВСЕ НАШТ ПОСТЫ


def get_post_list(db: Session):
    return db.query(Post).all()
# ФУНКЦИЯ СОЗДАНИЯ ПОСТА


def create_post(post_data: PostCreate, db: Session):
    post = Post(**post_data.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
