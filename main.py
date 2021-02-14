from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
from routes import routes
from core.db import SessionLocal

app = FastAPI()

#ПРОМЕЖУТОЧНЫЙ СЛОЙ КОТОРЫЙ ОТКРЫВАЕТ И ЗАКРЫВАЕТ СЕССИИ ПРИ КАЖДОМ ЗАПРОСЕ НА НАШЕ ПРИЛОЖЕНИЕ
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        #ОТКРЫТИЕ СЕСИИ
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        #ЗАКРЫТИЕ СЕССИИ
        request.state.db.close()
    return response

# ПОДКЛЮЧАЕМ К НАШЕМУ ПРИЛОЖЕНИЮ ВСЕ ЭНДПОИНТЫ, КОТОРЫЕ СОБРАЛИ
app.include_router(routes)
