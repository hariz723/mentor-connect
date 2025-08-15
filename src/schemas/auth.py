from pydantic import BaseModel
from typing import Optional, Any


class UserSchema(BaseModel):
    username: str
    password: str
    
class RegisterModel(BaseModel):
    username: str
    email: str
    password: str
    confirm_password: str
    created_at : Optional[Any] = None