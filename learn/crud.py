from sqlalchemy.orm import Session
from . import models, schemas
from .hashing import Hashing

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):

    #fake_hashed_password = user.password + "notreallyhashed"
    hashed_password = Hashing.set_password(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def get_item(db: Session, item_id:int):
    return db.query(models.Item).filter(models.Item.id == item_id ).first()

def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_user_item(db: Session, item_id: int):
    #db.query(models.Item).filter(models.Item.id == item_id).delete(synchronize_session=False)
    #db.commit()
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    db.delete(db_item)
    db.commit()
    return db_item

def update_item(db: Session, item_id: int, item: schemas.ItemUpdate):
    db.query(models.Item).filter(models.Item.id == item_id).update({'name': item.name, 'price': item.price, 'description': item.description})
    db.commit()
    return {"message": "updated"}