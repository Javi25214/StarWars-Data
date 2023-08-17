from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()

user_favorite_planet = Table(
    'user_favorite_planet', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('planet_id', Integer, ForeignKey('planets.id'))
)

user_favorite_character = Table(
    'user_favorite_character', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('character_id', Integer, ForeignKey('characters.id'))
)

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)  
    subscription_date = Column(String)  
    first_name = Column(String)
    last_name = Column(String)
    

    favorite_planets = relationship('Planet', secondary=user_favorite_planet, back_populates='favorited_by')
    

    favorite_characters = relationship('Character', secondary=user_favorite_character, back_populates='favorited_by')

class Planet(Base):
    __tablename__ = 'planets'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    climate = Column(String)
    terrain = Column(String)
    

    favorited_by = relationship('User', secondary=user_favorite_planet, back_populates='favorite_planets')

class Character(Base):
    __tablename__ = 'characters'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    height = Column(String)
    mass = Column(String)
    
    favorited_by = relationship('User', secondary=user_favorite_character, back_populates='favorite_characters')

Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

user = User(username='luke_skywalker', email='luke@example.com', password='password', subscription_date='2023-08-17', first_name='Luke', last_name='Skywalker')
planet = Planet(name='Tatooine', climate='Arid', terrain='Desert')
character = Character(name='Darth Vader', height='2.03m', mass='136kg')

user.favorite_planets.append(planet)
user.favorite_characters.append(character)

session.add(user)
session.add(planet)
session.add(character)
session.commit()

print("Base de datos creada y datos agregados.")