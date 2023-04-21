from server.src.schemas.entity import EntityDBSchema


class CheckDBSchema(EntityDBSchema):
    result: str
    is_attack: bool
    type_id: int
    person_id: int

    class Config:
        orm_mode = True
