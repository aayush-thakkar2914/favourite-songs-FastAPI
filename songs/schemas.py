from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime


# User input for registration
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

# User response model
class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True

class TokenData(BaseModel):
    email: str | None = None

# Song input
class SongCreate(BaseModel):
    title: str
    artist: str
    genre: str

# Song response model
class SongOut(SongCreate):
    id: int
    owner_id: int

    class Config:
        orm_mode = True



