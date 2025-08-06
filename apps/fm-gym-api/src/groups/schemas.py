from pydantic import BaseModel
from models import GroupBase, GroupScheduleBase

class CreateGroupSchema(GroupBase):
    schedule: list[GroupScheduleBase]

class ReadGroupSchema(GroupBase):
    id: int
    schedule: list[GroupScheduleBase]

class MCPGetGroupsFilterSchema(BaseModel):
    age: int

class MCPReadGroupSchema(BaseModel):
    name: str
    schedule: list[GroupScheduleBase]
