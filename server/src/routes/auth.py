import uuid

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import JSONResponse

from server.src.models.user import User
from server.src.schemas.auth import SignInSchema, SignUpSchema
from server.src.utils.auth import authenticate_user
from server.src.utils.crypt import get_password_hash
from server.src.utils.db import get_db, sessions

router = APIRouter(prefix='/auth')


@router.post("/sign-up/")
async def sign_up(registration_data: SignUpSchema,
                  db: Session = Depends(get_db)):
    """
    Registration (creation of a new user).
    Login immediately.
    """
    potentially_existing_user = db.query(User).filter(User.email == registration_data.email).first()

    if potentially_existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={"detail": "User with the same email address or account name already exists"}
        )

    user = User(
        email=registration_data.email,
        username=registration_data.username,
        password=get_password_hash(registration_data.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return await sign_in(
        SignInSchema(
            username=user.username,
            password=registration_data.password
        ),
        db
    )


@router.post("/sign-in/")
async def sign_in(login_data: SignInSchema,
                  db: Session = Depends(get_db)):
    """
    Sets the session id in the request cookie
    if the user is successfully authenticated.
    """
    user: User | None = await authenticate_user(login_data.username, login_data.password, db)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"detail": "Incorrect account name or password"}
        )

    session_id = str(uuid.uuid4())
    sessions[session_id] = user.id

    response = JSONResponse({"detail": "Logged in successfully"})
    response.set_cookie("session_id", session_id, max_age=3600)
    return response


@router.post('/sign-out/')
def sign_out():
    return {"message": "Sign out"}


@router.post('/me/')
def me():
    return {"message": "Me"}
