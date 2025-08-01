from datetime import time
from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

class GroupBase(SQLModel):
    name: str
    capacity: int
    ageStart: int
    ageEnd: int

class Group(GroupBase, table=True):
    id: int = Field(default=None, primary_key=True)
    schedule: List["GroupSchedule"] = Relationship(back_populates="group")

class GroupScheduleBase(SQLModel):
    day: int
    startTime: time
    endTime: time

class GroupSchedule(GroupScheduleBase, table=True):
    id: int = Field(default=None, primary_key=True)
    group_id: Optional[int] = Field(foreign_key="group.id")
    group: Optional[Group] = Relationship(back_populates="schedule")