import os
from os.path import dirname, expanduser
from urllib.parse import quote_plus

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

dotenv_path = expanduser("~/Documentos/proyectos/microred/.env")

load_dotenv(dotenv_path)


DB_USER = os.getenv("DB_USER")
print(DB_USER)
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD", ""))  # escapa caracteres como @ o #
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # verifica que la conexión siga viva antes de usarla
    pool_recycle=3600,  # evita el error "MySQL server has gone away"
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


class Base(DeclarativeBase):
    pass


# Dependencia para inyectar la sesión en los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
