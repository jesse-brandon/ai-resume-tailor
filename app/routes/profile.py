from fastapi import APIRouter

from app.schemas.profile import ProfileCreate
from domain.profile.repository import create_profile

router = APIRouter(prefix="/profile", tags=["Profile"])


@router.post("")
def create(profile: ProfileCreate):
    return create_profile(profile)
