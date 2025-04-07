from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models, schemas

def create(request: schemas.SongCreate, db: Session, user_id: int):
    new_song = models.Song(
        title=request.title,
        artist=request.artist,
        genre=request.genre,
        owner_id=user_id
    )
    db.add(new_song)
    db.commit()
    db.refresh(new_song)
    return new_song

def get_all(db: Session, genre: str = None):
    if genre:
        return db.query(models.Song).filter(models.Song.genre == genre).all()
    return db.query(models.Song).all()

def update(id: int, request: schemas.SongCreate, db: Session, user_id: int):
    song_query = db.query(models.Song).filter(models.Song.id == id, models.Song.owner_id == user_id)
    song = song_query.first()
    
    if not song:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Song not found")
    
    song_query.update(request.dict(), synchronize_session=False)
    db.commit()
    return song_query.first()

def destroy(id: int, db: Session, user_id: int):
    song = db.query(models.Song).filter(models.Song.id == id, models.Song.owner_id == user_id).first()
    
    if not song:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Song not found")
    
    db.delete(song)
    db.commit()
    return {"detail": "Song Deleted"}
