from fastapi import APIRouter, Depends, status, HTTPException
from app.schemas.summary import SummaryUpdateRequest
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from datetime import datetime

from app.core.database import get_session
from app.models.summary import Summary
from app.schemas.summary import SummaryCreate, SummaryUpdate, SummaryResponse
from app.services.llm_service import generate_summary

router = APIRouter(prefix="/summaries", tags=["Summaries"])

#POST – Create summary
@router.post("", response_model=SummaryResponse, status_code=201)
async def create_summary(
    payload: SummaryCreate,
    session: AsyncSession = Depends(get_session)
):
    summary_text = await generate_summary(payload.text)

    summary = Summary(
        original_text=payload.text,
        summary_text=summary_text,
        model_used="gpt-3.5-turbo"
    )

    session.add(summary)
    await session.commit()
    await session.refresh(summary)
    return summary


#GET – Fetch summary
@router.get("/{summary_id}", response_model=SummaryResponse)
async def get_summary(summary_id: UUID, session: AsyncSession = Depends(get_session)):
    summary = await session.get(Summary, summary_id)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")
    return summary


#PUT – Update summary
@router.put("/{summary_id}", response_model=SummaryResponse)
async def update_summary(
    summary_id: UUID,
    payload: SummaryUpdate,
    session: AsyncSession = Depends(get_session)
):
    summary = await session.get(Summary, summary_id)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")
    if payload.summary_text is not None:
        summary.summary_text = payload.summary_text

    if payload.model_used is not None:
        summary.model_used = payload.model_used

    summary.summary_text = payload.summary_text
    summary.updated_at = datetime.utcnow()

    await session.commit()
    await session.refresh(summary)
    
    return summary


#DELETE – Remove summary
@router.delete("/{summary_id}", status_code=204)
async def delete_summary(summary_id: UUID, session: AsyncSession = Depends(get_session)):
    summary = await session.get(Summary, summary_id)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")

    await session.delete(summary)
    await session.commit()
