from typing import Optional

from pydantic import BaseModel, EmailStr


class ProfileCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: Optional[str] = None
    location: Optional[str] = None
    is_active: Optional[bool] = True
