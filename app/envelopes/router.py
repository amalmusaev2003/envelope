from fastapi import APIRouter, Depends
from typing import List

from app.envelopes.dao import EnvelopeDAO
from app.envelopes.schemas import SEnvelope, SNewEnvelope, SUpdateEnvelope
from app.users.models import Users
from app.users.dependencies import get_current_user


router = APIRouter(
    prefix="/envelopes",
    tags=["Конверты"]
)

@router.get("")
async def get_envelopes(user: Users = Depends(get_current_user)) -> List[SEnvelope]:
    return await EnvelopeDAO.find_all(user_id=user.id)

@router.get("/{envelope_id}")
async def get_envelopes_by_id(
    envelope_id: int,
    user: Users = Depends(get_current_user)
) -> SEnvelope:
    return await EnvelopeDAO.find_one_or_none(envelope_id=envelope_id, user_id=user.id)

@router.post("")
async def add_envelope(
    envelope: SNewEnvelope,
    user: Users = Depends(get_current_user)
):
    return await EnvelopeDAO.add(name=envelope.name, description=envelope.description, user_id=user.id, balance=envelope.balance)

@router.delete("/{envelope_id}")
async def remove_envelope(
    envelope_id: int,
    user: Users = Depends(get_current_user)
):
    return await EnvelopeDAO.delete(id=envelope_id, user_id=user.id)

@router.patch("/{envelope_id}")
async def update_envelope(
    envelope_id: int,
    data: SUpdateEnvelope,
    user: Users = Depends(get_current_user)
):
    return await EnvelopeDAO.update(user.id, envelope_id, name=data.name, description=data.description, balance=data.balance)
    


