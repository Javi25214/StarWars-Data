import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    class Comment(Base):
        __tablename__ = "comment"
        post_id = Columm(Integer, FOreingKey ("post.id"), primary_key=True)
        comment_text = Column(String(250), nullable=False)
        author_id = Column(Integer, ForeignKey("user.id"))

class Post(Base):
    __tablename__ = "post"
    user_id = Column(Integer, ForeignKey('user.id'))
    id = Columm(Post)

class MediaEnum(enum.Enum):
    photo = 1
    video = 2

    class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    type = Column(Enum(MediaEnum))
    url = Column(String)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

    class Follower(Base):
    __tablename__ = "follower"
    id = Column(Integer, primary_key=True)
    user_from_id = Column (Integer, ForeignKey("user.id"))
    user_to_id = Column (Integer, ForeignKey("user.id"))


    def to_dict(self):
        return {}
    
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
