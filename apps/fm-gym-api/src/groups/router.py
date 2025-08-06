from typing import Annotated, Optional
from fastapi import APIRouter, Depends, Query
from sqlmodel import Session
from database import get_session
from dependencies import require_api_key

from .service import GroupService
from .schemas import CreateGroupSchema, ReadGroupSchema

def get_group_service(session: Annotated[Session, Depends(get_session)]) -> GroupService:
    return GroupService(session)

GroupServiceDep = Annotated[GroupService, Depends(get_group_service)]

router = APIRouter(
    prefix="/groups",
    tags=["groups"],
    dependencies=[Depends(require_api_key)],
)

@router.post("/", response_model=ReadGroupSchema)
def create_group(service: GroupServiceDep, group: CreateGroupSchema):
    return service.create_group(group)

@router.get("/", response_model=list[ReadGroupSchema])
def get_groups(
    service: GroupServiceDep,
    age: Annotated[int | None, Query(title='Age filter', description="Allow filtering the groups by age", gt=0)] = None,
    name: Annotated[str | None, Query(title='Name filter', description="Allow filtering the groups by name", min_length=1)] = None,
):
    return service.get_groups(age=age, name=name)

@router.get("/{group_id}", response_model=ReadGroupSchema)
def get_group_by_id(service: GroupServiceDep, group_id: int):
    return service.get_group_by_id(group_id)