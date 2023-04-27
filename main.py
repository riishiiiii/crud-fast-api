from fastapi import FastAPI
import models
from config import engine
from routes import router

models.Base.metadata.create_all(bind = engine)

app = FastAPI()


@app.get("/api")
def hello():
    return "Hello"  

app.include_router(router, prefix="/book", tags=["book"])