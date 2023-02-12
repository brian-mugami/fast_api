from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import crud, schemas
from learn import dependencies
from ..hashing import Hashing
from ..jwtfile import create_access_token

ACCESS_TOKEN_EXPIRE_MINUTES = 30
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
    dependencies=[Depends(dependencies.get_db)],
    responses={404: {"Description": "Not found"}}
)

@router.post("/login")
def login(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(dependencies.get_db)):
    user_indb = crud.get_user_by_email(email=user.username, db=db)
    if not user_indb:
        raise HTTPException(status_code=404, detail="User not found")
    if not Hashing.verify_password(user.password, user_indb.hashed_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Wrong Password!")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}