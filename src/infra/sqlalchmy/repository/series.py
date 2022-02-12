from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchmy.models import models

class RepositorySerie():

    def __init__(self, db:Session):
        self.db = db

    def create(self, serie: schemas.Serie):
        db_serie = models.Serie(
            title = serie.title,
            genre = serie.genre,
            seasons = serie.seasons
        )
        self.db.add(db_serie)
        self.db.commit()
        self.db.refresh(db_serie)
        return db_serie

    def list(self):
        series = self.db.query(models.Serie).all()
        return series
    
    def get(self, serie_id: int):
        stmt = select(models.Serie).filter_by(id=serie_id)
        serie = self.db.execute(stmt).scalars().one()

        return serie

    def get_title(self, serie_title: str):
        stmt = select(models.Serie).filter_by(title=serie_title)
        serie = self.db.execute(stmt).scalars().one()
        return serie


    def remove(self, serie_id: int):
        stmt = delete(models.Serie).where(models.Serie.id == serie_id)
       
        self.db.execute(stmt)
        self.db.commit()
