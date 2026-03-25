from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.responses import FileResponse

from domain.resume.pipeline import generate_resume

router = APIRouter()


@router.post("/generate-resume")
async def generate_resume_endpoint(file: UploadFile = File(...)):

    try:
        contents = await file.read()
        job_text = contents.decode("utf-8")

        pdf_path = generate_resume(job_text)

        return FileResponse(
            path=pdf_path, media_type="application/pdf", filename="resume.pdf"
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
