'''from fastapi import FastAPI
from sqlmodel import SQLModel
from app.core.database import engine
from app.routers.summary import router

app = FastAPI(title="AI Text Summarizer API")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

app.include_router(router)
'''

from fastapi import FastAPI
from app.routers.summary import router

app = FastAPI(title="AI Text Summarizer API")

app.include_router(router)
