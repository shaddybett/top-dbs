from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace 'sqlite:///example.db' with your desired database connection string
# For example, 'postgresql://username:password@localhost/dbname' for PostgreSQL
engine = create_engine('sqlite:///example.db', echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# Create the database tables
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Add a user to the database
new_user = User(name='John Doe', age=30)
session.add(new_user)
session.commit()

# Query the database
queried_user = session.query(User).filter_by(name='John Doe').first()
print(f'Queried User: {queried_user.name}, Age: {queried_user.age}')

# Close the session
session.close()
