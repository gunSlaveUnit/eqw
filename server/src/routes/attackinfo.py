import uuid
from typing import List, Type

from fastapi import APIRouter,  Depends
from sqlalchemy.orm import Session


from server.src.models.attack import Attack
from server.src.schemas.attack import AttackDBSchema
from server.src.utils.db import get_db, sessions

router = APIRouter(prefix='/attack')


@router.get('/{code}', response_model=AttackDBSchema)
async def attack_by_code(code: int | None = None,
                db: Session = Depends(get_db)) -> Type[Attack]:
    """
    Attacks with this code
    """
    return db.query(Attack).filter(Attack.id == code).one()


@router.get('/', response_model=List[AttackDBSchema])
async def every(db: Session = Depends(get_db)) -> list[Type[Attack]]:
    """
    All Attacks
    """
    return db.query(Attack).all()
