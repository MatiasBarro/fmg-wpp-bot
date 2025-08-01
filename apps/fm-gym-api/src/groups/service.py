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
    
    def get_groups(self) -> list[Group]:
        return self.session.exec(select(Group))
    
    def get_group_by_id(self, group_id: int) -> Group:
        statement = select(Group).where(Group.id == group_id)
        return self.session.exec(statement).first()
