import sys

# TODO: bad
sys.path.append("C:/eqw")

from fastapi import FastAPI

from server.src.utils.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
