from server.src.schemas.entity import EntityDBSchema


class UserDBSchema(EntityDBSchema):
    email: str
    username: str
    password: str

    class Config:
        from_attributes = True
