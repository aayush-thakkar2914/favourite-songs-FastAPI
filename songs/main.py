from fastapi import FastAPI
from .routers import users, authentication, songs

app = FastAPI()

app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(songs.router)

@app.get("/")
def home():
    return {"message": "Welcome to the Favourite Song Management API by Aayush Thakkar"}
