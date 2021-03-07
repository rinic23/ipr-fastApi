from fastapi import APIRouter
from microblog import blog
from user import users
# СОБИРАЕМ ВСЕ НАШИ ЭНДПОИНТЫ
routes = APIRouter()

routes.include_router(blog.router, prefix='/blog')
routes.include_router(users.router, prefix='/user')
