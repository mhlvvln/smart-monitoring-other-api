from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Config(Base):
    __tablename__ = 'config'
    id = Column(Integer, primary_key=True)
    expires_at = Column(Integer)
    expires_in = Column(Integer)
    access_token = Column(String)
