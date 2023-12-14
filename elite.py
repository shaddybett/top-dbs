from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid
# after the imports make a database
db = 'sqlite:///eliteDB.db'

def generate_uuid():
    return str (uuid.uuid4())

# create sqlalchemy engine
engine = create_engine(db,echo=True)

# defined a declarative base
Base = declarative_base()

class City(Base):
    __tablename__='cities'
    cityId = Column('cityId',String,primary_key=True,default=generate_uuid)
    cityName = Column('cityName',String)
    cityPopulation = Column('cityPopulation',)
