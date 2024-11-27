from fastapi import FastAPI
from . import models
from .database import engine

"""" 
FastAPI server with DB PostgreSQL installation and start
uvicorn sql_app.main:app --reload
"""
models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!!!"}
