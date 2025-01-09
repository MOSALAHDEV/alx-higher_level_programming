#!/usr/bin/python3
""" script that lists all State objects from the database hbtn_0e_6_usa """
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys


username = sys.argv[1]
password = sys.argv[2]
host = 'localhost'
port = '3306'
database = sys.argv[3]
Base = declarative_base()
engine = create_engine(f'mysql+mysqldb://{username}:{password}@{host}:{port}/{database}', echo=True)

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return f"<State(id={self.id}, name='{self.name}'>"

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
session.commit()
session.close()
