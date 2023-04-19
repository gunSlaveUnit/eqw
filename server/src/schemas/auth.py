from pydantic.main import BaseModel
from pydantic.networks import EmailStr


class SignInSchema(BaseModel):
    username: str
    password: str


class SignUpSchema(BaseModel):
    email: EmailStr
    username: str
    password: str
