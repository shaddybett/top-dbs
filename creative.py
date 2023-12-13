from sqlalchemy import create_engine,String,Column,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid
engine = create_engine('sqlite:///creativeDB.db')

Base = declarative_base()

def generate_uuid():
    return str (uuid.uuid4())
class Book(Base):
    __tablename__='books'
    bookId = Column('bookId',primary_key=True,default=generate_uuid)
    bookName = Column('bookName',String)
    bookPages = Column('bookPages',Integer)
    bookAuthor = Column('bookAuthor',String)

    @classmethod
    def add_book(cls,bookName,bookPages,bookAuthor):
        




