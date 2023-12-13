from sqlalchemy import create_engine,String,Column,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid
engine = create_engine('sqlite:///creativeDB.db')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

def generate_uuid():
    return str (uuid.uuid4())
class Book(Base):
    __tablename__='books'
    bookId = Column('bookId',String,primary_key=True,default=generate_uuid)
    bookName = Column('bookName',String)
    bookPages = Column('bookPages',Integer)
    bookAuthor = Column('bookAuthor',String)

    def __init__(self,bookName,bookPages,bookAuthor):
        self.bookName = bookName
        self.bookAuthor = bookAuthor
        self.bookPages = bookPages

    def add_book(self,bookName,bookPages,bookAuthor):
        exists = session.query(Book).filter(Book.bookName == bookName).all()
        if len(exists) > 0:
            print('Name already exists')
        else:
            new_Book = Book(bookName=bookName,bookPages=bookPages,bookAuthor=bookAuthor)
            session.add(new_Book)
            session.commit()
            print('New book added')    

new_Book = Book(bookName='The Art Of Coding',bookPages=400,bookAuthor='Kipkorir')
new_Book.add_book


