from contextlib import asynccontextmanager
from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from fastapi_mcp import FastApiMCP, AuthConfig
from database import create_db_and_tables
from dependencies import require_api_key

import models
from groups import group_router, mcp_router

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create the database tables
    create_db_and_tables()
    yield


app = FastAPI(
  root_path="/api/v1",
  lifespan=lifespan,
)

app.include_router(group_router)

mcp_app = FastAPI(
    lifespan=lifespan,
)

mcp_app.include_router(mcp_router)

# MCP app
mcp = FastApiMCP(
    mcp_app,
    name="FMG MCP", 
    description="Simple application to manage FM Gymnastics school groups",
    describe_all_responses=True,  # Include all possible response schemas
    describe_full_response_schema=True, # Include full JSON schema in descriptions
    auth_config=AuthConfig(
        dependencies=[Depends(require_api_key)],
    )
)

mcp.mount_http()

