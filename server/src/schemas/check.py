from server.src.schemas.entity import EntityDBSchema


class CheckDBSchema(EntityDBSchema):
    result: str
    is_attack: bool
    check_type: int
    person_id: int

    class Config:
        orm_mode = True


class CheckCreateSchema(EntityDBSchema):
    result: str
    is_attack: bool
    check_type: int

