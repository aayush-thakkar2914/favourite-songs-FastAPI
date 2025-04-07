from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, oauth2
from ..repository import songs

router = APIRouter(prefix="/songs", tags=["Songs"])
get_db = database.get_db

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_song(
    request: schemas.SongCreate,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    return songs.create(request, db, current_user.id)

@router.get("/", response_model=List[schemas.SongOut])
def get_songs(
    genre: str = None,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    return songs.get_all(db, genre)

@router.put("/{id}", response_model=schemas.SongOut)
def update_song(
    id: int,
    request: schemas.SongCreate,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    return songs.update(id, request, db, current_user.id)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_song(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    return songs.destroy(id, db, current_user.id)
