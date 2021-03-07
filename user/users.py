from fastapi import APIRouter, Depends
from .shemas import UserList, UserCreate
from .service import create_user_service, get_user_list
from sqlalchemy.orm import Session
from core.utils import get_db
from typing import List

router = APIRouter()


@router.get('/get-users', response_model=List[UserList])
def user_list(db: Session = Depends(get_db)):
    user_list = get_user_list(db)
    return user_list


@router.post('/create-users')
def post_list(post_data: UserCreate, db: Session = Depends(get_db)):
    return create_user_service(post_data, db)
