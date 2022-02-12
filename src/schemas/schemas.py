from pydantic import BaseModel
from typing import Optional, List

class Serie(BaseModel):
    id: Optional[str] = None
    title: str
    genre: str
    seasons: int

    class Config:
        orm_mode =  True
