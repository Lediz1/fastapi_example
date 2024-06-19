# from elasticsearch import Elasticsearch
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.util.compat import contextmanager

DATABASE_URL = "postgresql://user:password@database:5432/alpha"
# # ELASTICSEARCH_URL = "elasticsearch:///?Server=elasticsearch&Port=9200&User=elastic&Password=DkIedPPSCb"
# ELASTICSEARCH_URL = "elasticsearch:http//elasticsearch:9200"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# url = 'http://elastic:DkIedPPSCb@elasticsearch:9200'
# es = Elasticsearch(url)

# engine_es = create_engine(ELASTICSEARCH_URL)
# SessionLocalES = sessionmaker(bind=engine_es)

Base = declarative_base()


def get_db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


db_context = contextmanager(get_db_session)
