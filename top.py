from sqlalchemy import create_engine,String,Integer,Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

def generate_uuid():
    return str(uuid.uuid4)
Base = declarative_base()
class Movie(Base):
    __tablename__='movies'
    moviedId = Column('movieId',primary_key=True,)