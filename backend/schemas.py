# Pydantic schemas
from pydantic import BaseModel
from typing import List, Optional

class Metric(BaseModel):
    timestamp: str
    likes: Optional[int]
    comments: Optional[int]
    followers: Optional[int]

class Influencer(BaseModel):
    id: str
    name: str
    metrics: List[Metric]
