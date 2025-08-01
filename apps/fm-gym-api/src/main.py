from contextlib import asynccontextmanager
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from database import create_db_and_tables

import models
from groups import router as group_router

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


# @app.get("/bmi", operation_id="calculate_bmi", summary="this tool is used to calculate bmi based on weigth and height")
# def calculate_bmi(weight_kg: float, height_m: float):
#     return {"bmi": weight_kg / (height_m ** 2)}

# mcp = FastApiMCP(app, name="BMI MCP", description="Simple application to calculate BMI")
# mcp.mount()
