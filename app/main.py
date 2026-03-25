from fastapi import FastAPI

from app.routes.resume import router as resume_router

app = FastAPI(title="AI Resume Tailor")

app.include_router(resume_router)
