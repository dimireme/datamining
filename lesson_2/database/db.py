from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lesson_2.database.models import (Base, BlogPost, Writer, Tag)


class BlogDb:
    def __init__(self, url, base=Base):
        engine = create_engine(url)
        base.metadata.create_all(engine)
        session_db = sessionmaker(bind=engine)
        self.__session = session_db()

    @property
    def session(self):
        return self.__session


if __name__ == '__main__':
    db_url = 'sqlite:///blogpost.sqlite'
    db = BlogDb(db_url)

    # tags = [Tag(f'tag_{itm}') for itm in range(30)]
    # writers = [Writer(f'name_{itm}', f'url_{itm}') for itm in range(10, 40)]
    # blogpost = BlogPost('title1', 'url1', writers[5], tags[:5])
    # db.session.add(blogpost)
    # db.session.commit()
    # db.session.add_all(tags)
    # db.session.commit()

    # db.session.add(Tag('tag_1')) # приводит к ошибке, так как такое имя уже есть
    # db.session.rollback() # сбрасывает сессию, которая повисла из-за ошибки

    # db.session.query(BlogPost).all() # выборка всех объектов
    # tmp = db.session.query(BlogPost).first() # выборка первого объекта
    # tmp.writer.name
    # temp = db.session.query(Tag).filter_by(name='tag_1').all()

    print(1)
