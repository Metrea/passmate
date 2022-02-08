from typing import Optional

from pydantic import BaseModel, EmailStr

class RatingBase(BaseModel):
    user_id: int = None
    score: int = None
    body: Optional[str] = None


class RatingCreate(RatingBase):
    user_id: str
    score: int = None
    body: Optional[str] = None 


class RatingUpdate(RatingBase):
    user_id: str
    score: int = None
    body: Optional[str] = None


# Properties shared by models stored in DB
class RatingInDBBase(RatingBase):
    id: int
    user_id: int
    event_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Rating(RatingInDBBase):
    pass


# Properties properties stored in DB
class RatingInDB(RatingInDBBase):
    pass