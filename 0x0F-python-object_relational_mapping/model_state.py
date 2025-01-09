#!/usr/bin/python3
""" script that lists all State objects from the database hbtn_0e_6_usa """
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys


base = declarative_base()


class State(base):
    """ State class """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
            f'mysql+mysqldb://{username}:\
                    {password}@localhost/{database}', echo=True)
    Base.metadata.create_all(engine)
