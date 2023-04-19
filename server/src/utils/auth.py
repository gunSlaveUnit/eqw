from server.src.models.user import User
from server.src.utils.crypt import crypt_context


async def verify_password(plain_password, hashed_password):
    return crypt_context.verify(plain_password, hashed_password)


async def authenticate_user(username: str, password: str, db):
    user = db.query(User).filter(User.username == username).first()
    if user and await verify_password(password, user.password):
        return user
    return None
