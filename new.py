from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database connection URL (SQLite in this case)
DATABASE_URL = "sqlite:///.db"

# Create an SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Define a declarative base
Base = declarative_base()

# Define a simple User class as an example table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# --- Create Operation (Insert) ---

# Add a new user to the database
new_user = User(name="John Doe", age=25)
session.add(new_user)
session.commit()

# --- Read Operation (Query) ---

# Query and print all users in the database
users = session.query(User).all()
print("Read Operation:")
for user in users:
    print(f"User ID: {user.id}, Name: {user.name}, Age: {user.age}")

# --- Update Operation ---

# Update the age of the first user
user_to_update = session.query(User).first()
if user_to_update:
    user_to_update.age = 30
    session.commit()

    # Verify the update
    updated_user = session.query(User).filter_by(id=user_to_update.id).first()
    print("Update Operation:")
    print(f"User ID: {updated_user.id}, Name: {updated_user.name}, Updated Age: {updated_user.age}")

# --- Delete Operation ---

# Delete the second user (if exists)
user_to_delete = session.query(User).filter_by(id=2).first()
if user_to_delete:
    session.delete(user_to_delete)
    session.commit()

    # Verify the deletion
    remaining_users = session.query(User).all()
    print("Delete Operation:")
    for user in remaining_users:
        print(f"User ID: {user.id}, Name: {user.name}, Age: {user.age}")

# Close the session
session.close()
