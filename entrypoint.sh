alembic upgrade head
# alembic revision --autogenerate -m "New migration"
uvicorn main:app --reload --host 0.0.0.0 --port 27689