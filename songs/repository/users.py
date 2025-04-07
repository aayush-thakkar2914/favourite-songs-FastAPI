from sqlalchemy.orm import Session
from fastapi import HTTPException
from .. import models, schemas
from ..hashing import Hash

def create(user: schemas.UserCreate, db: Session):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = Hash.bcrypt(user.password)
    
    new_user = models.User(
        name=user.name,
        email=user.email,
        password=hashed_pw
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
