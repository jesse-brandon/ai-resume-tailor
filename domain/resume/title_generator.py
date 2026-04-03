import os

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_title(job_description: str) -> str:
    prompt = f"""
Extract a professional resume title from this job description.

Rules:
- Keep it short (3-6 words)
- Use standard industry titles
- No fluff

Examples:
"Senior Data Engineer"
"Database Administrator"
"Data Architect"

Job Description:
{job_description}

Title:
"""

    try:
        response = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[{"role": "user", "content": prompt}],
        )

        return (response.choices[0].message.content or "").strip()

    except Exception:
        return "Data Engineer"  # fallback        return "Data Engineer"  # fallback
