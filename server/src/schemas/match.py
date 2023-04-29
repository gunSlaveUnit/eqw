from server.src.schemas.entity import EntityDBSchema


class CheckDBSchema(EntityDBSchema):

    attack_id: int
    check_id: int

    class Config:
        orm_mode = True
