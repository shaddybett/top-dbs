from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# after the imports make a database
db = 'sqlite:///eliteDB.db'

# create sqlalchemy engine
engine = create_engine(db,echo=True)

# Base = declarative_base()
