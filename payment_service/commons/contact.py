__all__ = ["ContactInfo"]


from typing import Optional

from pydantic import BaseModel, EmailStr


class ContactInfo(BaseModel):
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
