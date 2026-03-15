from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()


class Student(Base):
    """Модель студента"""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    birth_date = Column(Date, nullable=True)
    enrollment_year = Column(
        Integer,
        nullable=False,
        default=datetime.datetime.now().year
    )


class Subject(Base):
    """Модель учебного предмета"""
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False, index=True)
    description = Column(String(500), nullable=True)
    credits = Column(Integer, nullable=False, default=3)
    department = Column(String(100), nullable=False, default="General")
