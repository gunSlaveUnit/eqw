from server.src.schemas.entity import EntityDBSchema


class MatchDBSchema(EntityDBSchema):

    attack_id: int
    check_id: int

    class Config:
        orm_mode = True
