from fastapi import APIRouter

router = APIRouter(prefix='/auth')


@router.post('/sign-up/')
def sign_up():
    return {"message": "Sign up"}


@router.post('/sign-in/')
def sign_in():
    return {"message": "Sign in"}


@router.post('/sign-out/')
def sign_out():
    return {"message": "Sign out"}


@router.post('/me/')
def me():
    return {"message": "Me"}
