from sqlalchemy import Column, Integer, String
from src.infra.sqlalchmy.config.database import Base

class Serie(Base):
    __tablename__ = 'series'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    genre = Column(String)
    seasons = Column(Integer)
