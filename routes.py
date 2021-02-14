from fastapi import APIRouter
from microblog import blog
# СОБИРАЕМ ВСЕ НАШИ ЭНДПОИНТЫ
routes = APIRouter()

routes.include_router(blog.router, prefix='/blog')
