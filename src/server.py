from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchmy.config.database import get_db, create_db
from src.infra.sqlalchmy.repository.series import RepositorySerie
from src.schemas.schemas import Serie

create_db()

app = FastAPI()

@app.get('/series')
def list_series(db: Session = Depends(get_db)):
    return RepositorySerie(db).list()

@app.post('/series')
def create_serie(serie: Serie, db: Session = Depends(get_db)):
    create_serie = RepositorySerie(db).create(serie)
    return create_serie

@app.get('/series/{serie_id}')
def get_serie(serie_id: int , db: Session = Depends(get_db)):
    serie = RepositorySerie(db).get(serie_id)
    return serie

@app.get('/series/name/{serie_title}')
def get_title(serie_title: str, db:Session = Depends(get_db)):
    serie_title = RepositorySerie(db).get_title(serie_title)
    return serie_title

@app.delete('/series/{serie_id}')
def remove_serie(serie_id: int , db: Session = Depends(get_db)):
    serie = RepositorySerie(db).remove(serie_id)
    return {'message': "Removido com sucesso!"}