from fastapi import FastAPI

from app.routes.data import router as data_router
from app.routes.resume import router as resume_router

app = FastAPI(title="AI Resume Tailor")

app.include_router(resume_router)
app.include_router(data_router)
