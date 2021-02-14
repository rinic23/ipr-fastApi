from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from . import service
from .shemas import PostCreate
from typing import List
from .shemas import PostList
router = APIRouter()

# СОЗДАЁМ ЭНДПОИНТ ПОЛУЧЕНИЯ ПОСТОВ


@router.get('/get-posts', response_model=List[PostList])
# ПРЕЖДЕ ЧЕМ НАША ФУНКЦИЯ ЗАПУСТИТСЯ  ВЫПОЛНЯEТСЯ ФУНКЦИЯ в Depends ДЛЯ ПОЛУЧЕНИЯ state НАШЕЙ БД
def post_list(db: Session = Depends(get_db)):
    post_list = service.get_post_list(db)
    return post_list


@router.post('/create-post')
# ПРЕЖДЕ ЧЕМ НАША ФУНКЦИЯ ЗАПУСТИТСЯ  ВЫПОЛНЯEТСЯ ФУНКЦИЯ в Depends ДЛЯ ПОЛУЧЕНИЯ state НАШЕЙ БД
def post_list(post_data: PostCreate, db: Session = Depends(get_db)):
    return service.create_post(post_data, db)
