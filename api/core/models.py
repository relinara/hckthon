from typing import Optional
from pydantic import BaseModel

class BaseRequest(BaseModel):
    accountId: str
    token: str

class BaseResponse(BaseModel):
    success: bool
    msg: str

class ErrorResponse(BaseResponse):
    success = False
    msg = "Алдаа гарлаа"