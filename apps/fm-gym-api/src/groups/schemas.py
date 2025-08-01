from models import GroupBase, GroupScheduleBase

class CreateGroupSchema(GroupBase):
    schedule: list[GroupScheduleBase]

class ReadGroupSchema(GroupBase):
    id: int
    schedule: list[GroupScheduleBase]
