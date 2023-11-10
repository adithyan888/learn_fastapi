from typing import Optional
from pydantic import BaseModel

class Location(BaseModel):
    city: str
    state : str | None = None
    country: str = 'us'