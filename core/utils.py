from starlette.requests import Request

#ФУНКЦИЯ КОТОРАЯ ЗАБИРАЕТ state БД
def get_db(request: Request):
    return request.state.db
