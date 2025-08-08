from fastapi import HTTPException
from sqlmodel import Session, select
from models import Group, GroupSchedule
from .schemas import CreateGroupSchema

class GroupService:
    def __init__(self, session: Session):
        self.session = session

    def create_group(self, group: CreateGroupSchema) -> Group:
        group_data = group.model_dump()
        group_schedule = [GroupSchedule(**schedule) for schedule in group_data["schedule"]]
        del group_data["schedule"]

        db_group = Group(**group_data, schedule=group_schedule)
        
        #save in db
        self.session.add(db_group)
        self.session.commit()
        self.session.refresh(db_group)

        return db_group
    
    def get_groups(self, age: int | None = None, name: str | None = None) -> list[Group]:
        statement = select(Group)
        if age:
            statement = statement.where(Group.ageEnd >= age, Group.ageStart <= age)
        
        if name:
            statement = statement.where(Group.name == name)
        
        return self.session.exec(statement)
    
    def get_group_by_id(self, group_id: int) -> Group:
        statement = select(Group).where(Group.id == group_id)
        group = self.session.exec(statement).first()
        if not group:
            raise HTTPException(status_code=404, detail="Group not found")
        
        return group
