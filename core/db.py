from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#ДЛЯ ЗАПУСКА ПРИЛОЖЕНИЯ В РУЧНУЮ
# SQLALCHEMY_DATABASE_URL = "postgresql://egor2:egor2@localhost/newDataBase"
#ДЛЯ ЗАПУСКА ПРИЛОЖЕНИЯ С DOCKER
SQLALCHEMY_DATABASE_URL = "postgresql://egor2:egor2@0.0.0.0/newDataBase"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
