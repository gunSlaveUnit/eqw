from pydantic import BaseModel

from server.src.schemas.entity import EntityDBSchema


class CheckDBSchema(EntityDBSchema):
    result: str
    is_attack: bool
    check_type: int
    person_id: int

    class Config:
        from_attributes = True


class CheckCreateSchema(BaseModel):
    result: str
    is_attack: bool
    check_type: int

