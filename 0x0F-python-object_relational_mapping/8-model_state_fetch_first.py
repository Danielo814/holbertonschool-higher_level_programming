#!/usr/bin/python3
"""
'8-model_state_fetch_first' module, uses sqlalchemy to list first state
object from a database
"""
if __name__ == '__main__':
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).first()
    if states:
        print("{}: {}".format(states.id, states.name))
    else:
        print("Nothing")
    session.close()
