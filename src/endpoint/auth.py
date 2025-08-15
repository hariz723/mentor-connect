from fastapi import APIRouter 
from src.schemas.auth import RegisterModel


router = APIRouter()


@router.post("/register")
async def register_user(
    user: RegisterModel
):
    pass 

        