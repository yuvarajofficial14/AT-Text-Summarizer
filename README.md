## Assumptions
- Authentication and authorization are out of scope.
- External LLM availability is assumed to be reliable.
- Input text size is expected to be within reasonable API limits.
- Concurrency conflicts are not handled explicitly at this scale.

## Design Decisions

### Database
PostgreSQL was chosen for reliable persistence. SQLAlchemy async ORM is used for non-blocking database access.

### Architecture
A layered architecture separates routers, services, models, and schemas to improve maintainability and testability.

### Validation
All request and response data is validated using Pydantic models to enforce strict schemas.

### External API
The LLM integration is isolated in a service layer and mocked during testing to ensure deterministic test results.

## Solution Approach

1. Client sends text to the POST endpoint.
2. Request data is validated using Pydantic.
3. Text is sent to an external LLM service for summarization.
4. The original text and generated summary are stored in PostgreSQL.
5. Client can retrieve, update, or delete summaries using REST endpoints.

## Error Handling Strategy
- Invalid input data returns HTTP 422.
- Missing records return HTTP 404.
- Database errors are handled via FastAPI’s exception handling.
- External API failures can be retried or mocked during tests.

## How to Run the Project

### Setup
```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python create_tables.py
uvicorn app.main:app --reload
```
##ADD `.env.example` 

Create this file in **project root**.
'.env.example`
```
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/summarizer_db
OPENAI_API_KEY=API_KEY
OPENAI_BASE_URL=https://llm.com/
```
