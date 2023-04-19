import sys

# TODO: bad
sys.path.append("C:/eqw")

from fastapi import FastAPI, APIRouter

from server.src.utils.db import Base, engine
from server.src.routes.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

router = APIRouter()
router.include_router(auth_router)

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
