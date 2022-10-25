from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from typing import List

from workshop.services.auth import AuthService, get_current_user


from workshop.models.auth import (
    UserCreate,
    Token,
    User
)

router = APIRouter(prefix='/auth',
                   )


@router.post('/sign-up', response_model=Token)
def sign_up(user_data: UserCreate, service: AuthService = Depends()):
    return service.register_new_user(user_data)


@router.post('/sign-in', response_model=Token)
def sign_in(form_data: OAuth2PasswordRequestForm = Depends(), service: AuthService = Depends()):
    return service.authenticate_user(
        form_data.username,
        form_data.password
    )


@router.get('/user', response_model=User)
def get_user(user: User = Depends(get_current_user)):
    return user


@router.get('/users', response_model=List[User])
def get_users(service: AuthService = Depends()):
    return service.get_users()

