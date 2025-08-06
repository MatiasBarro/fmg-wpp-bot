from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader
from sqlmodel import Session, select

from database import get_session
from models import ApiKeys

api_key_header = APIKeyHeader(name="X-API-KEY")

def require_api_key(
        session: Annotated[Session, Depends(get_session)],
        api_key: Annotated[str, Depends(api_key_header)]) -> ApiKeys:
    
    db_api_key = session.exec(select(ApiKeys).where(ApiKeys.key == api_key)).first()
    if not db_api_key or db_api_key.enabled == False:
        raise HTTPException(status_code=401, detail="Not authorized")
    
    return db_api_key
    
