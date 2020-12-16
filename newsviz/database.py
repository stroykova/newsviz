import logging

from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine, Column, UnicodeText, Integer, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


logger = logging.getLogger(__name__)
Base = declarative_base()


class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    text = Column(UnicodeText)


class NewsVizDb:
    def __init__(self, uri: str):
        logger.info('Migrating database...')
        command.upgrade(Config("alembic.ini"), "head")
        logger.info('Migration done')
        engine = create_engine(uri)
        self.Session = sessionmaker(engine)

    def get_news_count(self):
        session = self.Session()
        return session.query(News).count()


