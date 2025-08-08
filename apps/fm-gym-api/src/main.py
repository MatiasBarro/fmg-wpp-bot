from contextlib import asynccontextmanager
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, FastAPI
from fastapi_mcp import FastApiMCP, AuthConfig
from database import create_db_and_tables
from dependencies import require_api_key

import models
from health_check import health_check_router
from groups import group_router, mcp_router

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create the database tables
    create_db_and_tables()
    yield


app = FastAPI(
  root_path="/api",
  lifespan=lifespan,
)

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(group_router)
v1_router.include_router(mcp_router)

app.include_router(v1_router)
app.include_router(health_check_router)

# MCP app
mcp = FastApiMCP(
    app,
    include_tags=['mcp'],
    name="FMG MCP", 
    description="Simple application to manage FM Gymnastics school groups",
    describe_all_responses=True,  # Include all possible response schemas
    describe_full_response_schema=True, # Include full JSON schema in descriptions
    auth_config=AuthConfig(
        dependencies=[Depends(require_api_key)],
    )
)

mcp.mount_http()

