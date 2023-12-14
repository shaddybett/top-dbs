from sqlalchemy import create_engine,String,Integer,Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

def generate_uuid():
    return str(uuid.uuid4)
Base = declarative_base()
class Movie(Base):
    __tablename__='movies'
    moviedId = Column('movieId',primary_key=True,default=generate_uuid)
    movieName = Column('movieNmae',String)
    movieWriter = Column('movieAuthor',String)

    def __init__(self,movieName,movieWriter):
        self.movieName = movieName
        self.movieWriter = movieWriter

def add_movie(movieName,movieWriter):
    exists = session.query(Movie).filter_by(movieName=movieName).all()
    if exists:
        print('Name already exists')
    else:
        new_movie = Movie(movieName,movieWriter)
        session.add(new_movie)
        session.commit()

db = 'sqlite:///movieDB.db'
engine = create_engine(db)
Session = sessionmaker(bind=engine)
session = Session()            