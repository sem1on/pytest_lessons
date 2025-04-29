from pydantic import BaseModel, field_validator

from src.enums.user_enam import Gender, Status

class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Gender
    status: Status

    @field_validator("email")
    def check_email_address(cls, v):
        if "@" in v:
            return v
        else:
            raise ValueError("Email not found")
