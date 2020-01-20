from sqlalchemy import (Table, Column, ForeignKey, String, Integer, DateTime)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# промежуточная таблица связи тегов и постов
assoc_post_tag = Table(
    'post_tag',
    Base.metadata,
    Column('blogpost_id', Integer, ForeignKey('blogpost.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)


# класс записи в блоге
class BlogPost(Base):
    __tablename__: str = 'blogpost'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String, unique=True)
    title = Column(String)
    date = Column(DateTime)
    writer_id = Column(Integer, ForeignKey('writer.id'))
    writer = relationship('Writer', backref='blogposts')
    tags = relationship('Tag', secondary=assoc_post_tag, backref='blogposts')

    def __init__(self, title: str, url: str, writer, tags=tuple()):
        self.title = title
        self.url = url
        self.writer = writer
        if tags:
            self.tags.extend(tags)


# класс автора поста
class Writer(Base):
    __tablename__ = 'writer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String, unique=True)
    name = Column(String)

    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url


# класс  для объекта тега
class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)

    def __init__(self, name: str):
        self.name = name
