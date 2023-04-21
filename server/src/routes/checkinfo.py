import uuid
from typing import List, Type

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from server.src.models.attack import Attack
from server.src.models.check import Check
from server.src.schemas.check import CheckDBSchema
from server.src.utils.db import get_db, sessions

router = APIRouter(prefix='/check')


@router.get('/type/{code}', response_model=List[CheckDBSchema])
async def check_by_type_code(code: int | None = None,
                             db: Session = Depends(get_db)) -> list[Type[Check]]:
    """
    Attacks with this code of type
    """
    return db.query(Attack).filter(Check.type_id == code).one()


@router.get('/pers/{code}', response_model=List[CheckDBSchema])
async def check_by_person_code(code: int | None = None,
                               db: Session = Depends(get_db)) -> list[Type[Check]]:
    """
    Attacks with this code of type
    """
    checks = db.query(Check)
    if code:
        check = checks.filter(Check.person_id == code).first()
        if check:
            return [check]
        else:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Check by this person not found")
    return checks.all()



@router.get('/', response_model=List[CheckDBSchema])
async def every(db: Session = Depends(get_db)) -> list[Type[Check]]:
    """
    All checks
    """
    return db.query(Check).all()
