#!/usr/bin/python3
"""
Script that lists all States
"""


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{0}:{1}@localhost/{2}\
        ".format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
