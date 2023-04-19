from server.src.schemas.entity import EntityDBSchema


class UserDBSchema(EntityDBSchema):
    email: str
    username: str
    password: str

    class Config:
        orm_mode = True
