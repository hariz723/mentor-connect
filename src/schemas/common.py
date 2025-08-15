from pydantic import BaseModel
from typing import Optional, Any


class SuccessResponse(BaseModel):
    status_code: int
    message: str
    data : Optional[Any] = None
    
class ErrorResponse(BaseModel):
    status_code: int
    message: str
    error_message : Optional[Any] = None
    
