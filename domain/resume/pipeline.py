from domain.job.ingest import ingest_job
from domain.resume.builder import build_resume
from domain.rewrite.rewriter import rewrite_bullets
from domain.scoring.ranker import rank_bullets
from infrastructure.embeddings.provider import embed_text
from infrastructure.pdf.renderer import render_pdf


def generate_resume(job_text: str):

    job = ingest_job(job_text)

    job_embedding = embed_text(job)

    bullets = rank_bullets(job_embedding)
    bullets = rewrite_bullets(bullets, job)

    resume_data = build_resume([{"achievement": b} for b in bullets])

    pdf_path = render_pdf(resume_data)

    return pdf_path
