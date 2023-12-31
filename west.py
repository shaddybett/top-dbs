from sqlalchemy import create_engine,String,Column,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

db = 'sqlite:///coders.db'
engine = create_engine(db,echo=False)

def generate_uuid():
    return str(uuid.uuid4())
Base = declarative_base()
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


class Pet(Base):
    __tablename__='pets'
    petId = Column('petId',String,primary_key=True,default=generate_uuid)
    petName = Column('petName',String)
    petAge = Column('petAge',Integer)

    def __init__(self,petName,petAge):
        self.petName = petName
        self.petAge = petAge

def add_pet(petName,petAge):
        
        exists = session.query(Pet).filter_by(petName=petName).all()
        if exists:
            print('Pet exists')
        else:
            new_pet = Pet(petName,petAge)
            session.add(new_pet)
            session.commit()
            print('Pet added to the database')



petName = 'sky'
petAge = 10
add_pet(petName,petAge)         
                
