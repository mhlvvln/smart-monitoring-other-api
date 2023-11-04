from sqlalchemy import create_engine

from dotenv import load_dotenv
import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from models import Config

load_dotenv()

Base = declarative_base()


def create_session():
    db_url = os.getenv("DATABASE_URL")
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    return Session()


def get_config(session):
    result = session.query(Config).filter_by(id=1).first()
    return result


def set_config(session, expires_at, expires_in, access_token):
    config = session.query(Config).filter_by(id=1).first()

    config.expires_at = expires_at
    config.expires_in = expires_in
    config.access_token = access_token
    session.commit()

    return config