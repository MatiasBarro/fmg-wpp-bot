from datetime import datetime,timezone 
from sqlmodel import Field, SQLModel

class ApiKeys(SQLModel, table=True):
    key: str = Field(primary_key=True)
    enabled: bool = Field(default=True)
    created_at: datetime = Field(default=datetime.now(timezone.utc), nullable=False)