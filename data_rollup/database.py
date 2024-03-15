from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data_rollup.models import Base

engine = create_engine('postgresql://practice_rw@localhost/practice_data_sa')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

def get_session():
    return Session()
