import uuid
from typing import List, Type

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import desc
from sqlalchemy.orm import Session
from starlette import status

from server.src.models.attack import Attack
from server.src.models.check import Check
from server.src.models.match import Match
from server.src.routes.auth import get_current_user
from server.src.schemas.check import CheckDBSchema, CheckCreateSchema
from server.src.schemas.match import MatchDBSchema, MatchCreateSchema
from server.src.utils.db import get_db, sessions

router = APIRouter(prefix='/check')


@router.get('/', response_model=List[CheckDBSchema])
async def every(db: Session = Depends(get_db)) -> list[Type[Check]]:
    return db.query(Check).all()


@router.get('/checks/', response_model=List[CheckDBSchema])
async def attack_by_user(code: int | None = None,
                         current_user=Depends(get_current_user),
                         db: Session = Depends(get_db)) -> Type[Check]:
    """
    Attacks by user
    """
    return db.query(Check).filter(current_user.id == Check.person_id).all()


@router.get('/last/', response_model=CheckDBSchema)
async def last_check(current_user=Depends(get_current_user),
                     db: Session = Depends(get_db)) -> Type[Check]:
    """
    Attacks by user last
    """
    return db.query(Check).filter(current_user.id == Check.person_id).order_by(desc(Check.created_at)).first()


@router.get('/checks/', response_model=List[CheckDBSchema])
async def attack_by_params(code: int | None = None,
                           current_user=Depends(get_current_user),
                           db: Session = Depends(get_db)) -> Type[Check]:
    """
    Attacks by user
    """
    return db.query(Check).filter(current_user.id == Check.person_id).all()


@router.post('/checks/', response_model=CheckDBSchema)
async def create(item: CheckCreateSchema,
                 db: Session = Depends(get_db),
                 current_user=Depends(get_current_user)):
    item = Check(**vars(item))
    item.person_id = current_user.id
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.post('/matchs/', response_model=MatchDBSchema)
async def create(item: MatchCreateSchema,
                 db: Session = Depends(get_db)):
    item = Match(**vars(item))
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.get('/check/', response_model=List[CheckDBSchema])
async def attack_by_params(start_time: int = Query(None),
                           end_time: int = Query(None),
                           search_type: int = Query(None),
                           current_user=Depends(get_current_user),
                           db: Session = Depends(get_db)) -> Type[Check]:
    print("attack_by_params was called")
    items_query = db.query(Check)
    items_query = items_query.filter(current_user.id == Check.person_id)
    if start_time is not None:
        items_query = items_query.filter(start_time <= Check.created_at)
    if end_time is not None:
        items_query = items_query.filter(end_time >= Check.created_at)
    if search_type is not None and search_type != 2:
        if search_type == 0:
            search_type = False
        if search_type == 1:
            search_type = True
        items_query = items_query.filter(search_type == Check.is_attack)

    items = items_query.all()
    print(items)
    return items
