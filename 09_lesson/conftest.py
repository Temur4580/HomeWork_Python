import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import DATABASE_URL
from models import Base, Student, Subject

@pytest.fixture
def engine():
    """Создает движок базы данных"""
    test_engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=test_engine)
    yield test_engine
    Base.metadata.drop_all(bind=test_engine)

@pytest.fixture
def db_session(engine):
    """Создает сессию для тестов"""
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.rollback()
    session.close()

@pytest.fixture
def sample_student(db_session):
    """Создает тестового студента"""
    student = Student(
        first_name="Иван",
        last_name="Петров",
        email="ivan@test.com"
    )
    db_session.add(student)
    db_session.commit()
    return student

@pytest.fixture
def sample_subject(db_session):
    """Создает тестовый предмет"""
    subject = Subject(
        name="Математика",
        description="Высшая математика",
        credits=5,
        department="Физико-математический"
    )
    db_session.add(subject)
    db_session.commit()
    return subject