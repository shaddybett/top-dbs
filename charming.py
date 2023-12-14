from sqlalchemy import create_engine,String,Column,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

db = 'sqlite:///charmingDB.db'
engine = create_engine(db,echo=True)

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())
class Student(Base):
    __tablename__='students'
    studentId = Column('studentId',String,primary_key=True,default=generate_uuid)
    studentName = Column('studentName',String)
    studentEmail = Column('studentEmail',String)
    studentAge = Column('studentAge',Integer)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_student (session,studentName,studentEmail,studentAge):
        exists = session.query(Student).filter_by(studentName=studentName).first()
        if exists:
             print('Name already exists')
        else:
            new_student = Student(studentName=studentName,studentEmail=studentEmail,studentAge=studentAge)
            session.add(new_student)
            session.commit()
student_list = [{'Name':'Ann','Email':'ann@gmail.com','Age':17},
                {'Name':'Bett','Email':'bett@gmail.com','Age':19},
                {'Name':'Mark','Email':'mark@gmail.com','Age':17},
                {'Name':'mane','Email':'mane@gmail.com','Age':28},
                {'Name':'Rocio','Email':'rocio@gmail.com','Age':10},
                {'Name':'Slim','Email':'slim@gmail.com','Age':31}]            
for member in student_list:
    add_student(session,studentName=member['Name'],studentEmail=member['Email'],studentAge=member['Age'])
session.close()

