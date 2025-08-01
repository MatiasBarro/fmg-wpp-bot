from typing import Annotated
from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session

from .service import GroupService
from .schemas import CreateGroupSchema, ReadGroupSchema

def get_group_service(session: Annotated[Session, Depends(get_session)]) -> GroupService:
    return GroupService(session)

GroupServiceDep = Annotated[GroupService, Depends(get_group_service)]

router = APIRouter(
    prefix="/groups",
    tags=["groups"],
)

@router.post("/", response_model=ReadGroupSchema)
def create_group(service: GroupServiceDep, group: CreateGroupSchema):
    return service.create_group(group)

@router.get("/", response_model=list[ReadGroupSchema])
def get_groups(service: GroupServiceDep):
    return service.get_groups()

@router.get("/{group_id}", response_model=ReadGroupSchema)
def get_group_by_id(service: GroupServiceDep, group_id: int):
    return service.get_group_by_id(group_id)