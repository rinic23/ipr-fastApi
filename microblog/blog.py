from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
router = APIRouter()

# СОЗДАЁМ ЭНДПОИНТ ПОЛУЧЕНИЯ ПОСТОВ


@router.get('/')
# ПРЕЖДЕ ЧЕМ НАША ФУНКЦИЯ ЗАПУСТИТСЯ  ВЫПОЛНЯEТСЯ ФУНКЦИЯ в Depends ДЛЯ ПОЛУЧЕНИЯ state НАШЕЙ БД
def post_list(db: Session = Depends(get_db)):
    print(db)
    return {}
