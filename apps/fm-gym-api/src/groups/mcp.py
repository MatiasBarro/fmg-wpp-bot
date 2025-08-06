from fastapi import APIRouter, Body, Depends

from .schemas import MCPGetGroupsFilterSchema, MCPReadGroupSchema
from .router import GroupServiceDep

router = APIRouter(tags=["groups", "mcp"])

@router.post("/get_groups", response_model=list[MCPReadGroupSchema], operation_id="get_groups", summary="Get all available groups")
def get_groups(
    service: GroupServiceDep,
    filter: MCPGetGroupsFilterSchema,
):
    return service.get_groups(age=filter.age)
    