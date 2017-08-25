from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings


DeclarativeBase = declarative_base()


def db_connect():
    """
    Laczy sie z baza za pomoca zadeklarowanej
    bazy w settings.py
    """
    return create_engine(URL(**settings.DATABASE))


def create_dane_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class Dane(DeclarativeBase):
    """Model mojej bazy"""
    __tablename__ = "dane"

    id = Column(Integer, primary_key=True)
    text = Column('text', String)
    author = Column('author', String)
