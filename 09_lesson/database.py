import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError

load_dotenv()

# Загрузка настроек из переменных окружения
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "postgres")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

# Формируем строку подключения
DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@"
    f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Создаем движок SQLAlchemy
engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_size=5,
    max_overflow=10
)

# Создаем фабрику сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
    """
    Создает и возвращает сессию базы данных.
    Сессия должна быть закрыта после использования.
    """
    db = SessionLocal()
    try:
        return db
    except SQLAlchemyError as e:
        db.close()
        raise e


def init_db():
    """Инициализация базы данных (создание таблиц)"""
    from models import Base
    Base.metadata.create_all(bind=engine)
