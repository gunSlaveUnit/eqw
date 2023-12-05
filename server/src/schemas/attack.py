from server.src.schemas.entity import EntityDBSchema


class AttackDBSchema(EntityDBSchema):
    type: str
    info: str

    class Config:
        from_attributes = True
