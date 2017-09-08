from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

from . import settings


DeclarativeBase = declarative_base()


def db_connect():
    """
    connect to database
    declarated in settings.py
    """
    return create_engine(URL(**settings.DATABASE))


def create_data_table(engine):

    DeclarativeBase.metadata.create_all(engine)


class Data(DeclarativeBase):
    """Database model"""
    __tablename__ = "data"

    id = Column(Integer, primary_key=True)
    text = Column('text', String)
    author = Column('author', String)
