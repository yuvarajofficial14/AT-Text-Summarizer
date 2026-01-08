from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class SummaryCreate(BaseModel):
    text: str = Field(min_length=50, max_length=5000)

class SummaryUpdate(BaseModel):
    summary_text: str = Field(min_length=10)

class SummaryResponse(BaseModel):
    id: UUID
    original_text: str
    summary_text: str
    model_used: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
