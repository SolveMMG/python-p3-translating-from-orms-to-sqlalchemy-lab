#!/usr/bin/env python3

from sqlalchemy import (Column, String, Integer, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Dog(Base):
    engine = create_engine("sqlite:///:memory:")
    Session =  sessionmaker(bind=engine)
    session =  Session()
    __tablename__ = 'dogs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())
