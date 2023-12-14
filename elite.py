from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid
# after the imports make a database
db = 'sqlite:///eliteDB.db'

def generate_uuid():
    return str(uuid.uuid4())

# create sqlalchemy engine
engine = create_engine(db,echo=True)

# defined a declarative base
Base = declarative_base()

class City(Base):
    __tablename__='cities'
    cityId = Column('cityId',String,primary_key=True,default=generate_uuid)
    cityName = Column('cityName',String)
    cityPopulation = Column('cityPopulation',String)
    cityBoss = Column('cityBoss',String)

Base.metadata.create_all(engine)  

Session = sessionmaker(bind=engine)
session = Session()

def add_city(session,cityName,cityPopulation,cityBoss):
    new_city = session.query(City).filter_by(City.cityName == cityName).all()
    if len(new_city)>0:
        print('Name already exists')
    else:
        new_city = City(cityName=cityName,cityPopulation=cityPopulation,cityBoss=cityBoss)
        session.add(new_city)
        session.commit()

city_data = [{'name':'Berlin','population':100000,'boss':'Professor'},
             {'name':'Denver','population':500000,'boss':'T.Charlie'},
             {'name':'Nairobi', 'population': 9000000,'boss':'Cooper'}]

for data in city_data:
    add_city(session,cityName=data['name'],cityPopulation=data['population'],cityBoss=data['boss'])

added_cities = session.query(City).all()
print('Cities added')

for city in added_cities:
    print(f"City ID: {city.cityId}, Name: {city.cityName}, Population: {city.cityPopulation}, Boss: {city.cityBoss}")

    def update_cities(session,old_Boss,new_Boss):
        cities_to_update = session.query(City).filter_by(cityBoss = old_Boss).all()

        if cities_to_update:
            for city in cities_to_update:
                city.cityBoss = new_Boss
            session.commit()
            print(f"Cities with Boss '{old_Boss}' updated to 'new_Boss'")
        else:
            print('No such city')
            
    def delete_city(session,cityName):
        city_to_delete      
session.close()