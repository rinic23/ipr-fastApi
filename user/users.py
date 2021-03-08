from fastapi import APIRouter, Depends
from .shemas import UserList, UserCreate
from .service import create_user_service, get_user_list, get_user_by_id_service, update_user_by_id_service
from sqlalchemy.orm import Session
from core.utils import get_db
from typing import List

router = APIRouter()


@router.get('/get-users', response_model=List[UserList])
def user_list(db: Session = Depends(get_db)):
    user_list = get_user_list(db)
    return user_list


@router.get('/get-user/{id}')
def user_by_id(id: int, db: Session = Depends(get_db)):
    user = get_user_by_id_service(db, id)
    return user


@router.post('/create-users')
def create_user(post_data: UserCreate, db: Session = Depends(get_db)):
    return create_user_service(post_data, db)


@router.put('/edit-user/{id}')
def update_user(post_data: UserCreate, id: int, db: Session = Depends(get_db)):
    return update_user_by_id_service(post_data, db, id)
