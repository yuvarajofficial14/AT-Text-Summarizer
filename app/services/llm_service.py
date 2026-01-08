import httpx
from app.core.config import settings
from fastapi import HTTPException
'''
async def generate_summary(text: str) -> str:
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.post(
                f"{settings.OPENAI_BASE_URL}/chat/completions",
                headers={
                    "Authorization": f"Bearer {settings.OPENAI_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gpt-3.5-turbo",
                    "messages": [
                        {"role": "system", "content": "Summarize the text."},
                        {"role": "user", "content": text}
                    ]
                }
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
    except Exception:
        raise HTTPException(status_code=502, detail="LLM API unavailable")
'''
async def generate_summary(text: str) -> str:
    return "Mocked summary"
