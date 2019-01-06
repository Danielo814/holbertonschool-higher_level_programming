#!/usr/bin/python3
"""
'10-model_state_my_get' module, uses sqlalchemy to list state
objects from a database
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
    states = session.query(State).filter(State.name == sys.argv[4]).first()
    if states:
        print("{}".format(states.id))
    else:
        print("Not found")
    session.close()
