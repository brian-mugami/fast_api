from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from .. import schemas,crud, dependencies

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    dependencies=[Depends(dependencies.get_db)],
    responses={404: {"Description": "Not found"}}
)

@router.post("/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(dependencies.get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@router.get("/", response_model=list[schemas.User], status_code=status.HTTP_200_OK)
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.User, status_code=status.HTTP_200_OK)
def read_user(user_id: int, db: Session = Depends(dependencies.get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/{user_id}/items/", response_model=schemas.Item, status_code=status.HTTP_201_CREATED, tags=["Custom"])
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(dependencies.get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)
