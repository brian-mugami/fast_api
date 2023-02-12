from pydantic import BaseModel
from typing import Optional
class ItemBase(BaseModel):
    name: str
    price: float
    description: Optional[str]

class ItemUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None

class ItemCreator(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner: ItemCreator
    class Config:
        orm_mode=True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True

class Login(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None