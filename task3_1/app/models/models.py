from pydantic import BaseModel, computed_field, EmailStr
from typing import Union

class User(BaseModel):
    
    name: str
    age: int

    @computed_field
    def is_adult(self) -> float:
        return self.age >= 18
    

class Feedback(BaseModel):
    name: str
    message: str


class UserCreate(BaseModel):

    name: str
    email: EmailStr
    age: Union[int, None] = None
    is_subscribed: Union[bool, None] = None


class Product(BaseModel):

    product_id: int
    name: str
    category: str
    price: float
