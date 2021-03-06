migrations_run:
	docker exec -it ipr-fastapi_web_1 bash -ac 'alembic upgrade head'
migrations_create:
	docker exec -it ipr-fastapi_web_1 bash -ac 'alembic revision --autogenerate -m "make migration"'	

