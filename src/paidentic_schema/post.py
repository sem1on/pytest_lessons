from pydantic import BaseModel, field_validator, Field


class Post(BaseModel):
    id: int 
    title: str

    # @field_validator("id")
    # def check_id_less_then_two(cls, v):
    #     if v > 2:
    #         raise ValueError("Id is not less then two")
    #     else:
    #         return v