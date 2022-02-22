from tokenize import Token
from fastapi import Depends, status, HTTPException
from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas,dababase,models
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from .config import settings
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
# Secret Key
# Algorithm
# Expriration time

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


def create_access_token(data: dict):
    to_endocde = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_endocde.update({"exp": expire})

    encoded_jwt = jwt.encode(to_endocde, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_acess_token(token: str, credentails_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")

        if id is None:
            raise credentails_exception

        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credentails_exception
    return token_data


def get_current_users(token: str = Depends(oauth2_scheme), db: Session = Depends(dababase.get_db)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail="Could not validate Credentails", headers={"WWW-Authenticate token:": "Bearer"})

    token = verify_acess_token(token, credential_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()
    return user
