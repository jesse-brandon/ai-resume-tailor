from domain.bullets.repository import fetch_all_bullets
from domain.job.ingest import ingest_job
from domain.resume.builder import build_resume
from domain.scoring.ranker import score_achievements


def generate_resume(job_text: str):

    job = ingest_job(job_text)

    bullets = fetch_all_bullets()

    scored = score_achievements(bullets, job)

    resume = build_resume(scored)

    return resume
