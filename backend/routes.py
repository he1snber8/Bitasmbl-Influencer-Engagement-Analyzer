# API routes
from fastapi import APIRouter
from .schemas import Influencer

router = APIRouter()

@router.get('/influencer/{id}')
async def get_influencer(id: str):
    # TODO: call services.fetch_profile and compute metrics
    return {"id": id}

@router.get('/search')
def search(q: str = ""):
    # TODO: implement search across cached profiles
    return {"query": q, "results": []}
