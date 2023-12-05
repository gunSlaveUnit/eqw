from pydantic import BaseModel

from server.src.schemas.entity import EntityDBSchema


class MatchDBSchema(EntityDBSchema):
    attack_id: int
    check_id: int

    class Config:
        from_attributes = True


class MatchCreateSchema(BaseModel):
    attack_id: int
    check_id: int
