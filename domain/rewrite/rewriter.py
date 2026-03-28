import os

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def rewrite_bullets(bullets: list, job_description: str) -> list:

    bullet_texts = [b["text"] for b in bullets]

    prompt = f"""
You are a senior technical resume writer.

Rewrite each bullet to be:
  concise (max 2 lines)
  impact-focused (include outcome or result)
  aligned to the job description keywords
  truthful (do NOT invent or exaggerate)

Use strong action verbs.

Job Description:
{job_description}

Bullets:
{bullet_texts}

Return rewritten bullets as a list in the same order.
"""

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    rewritten_texts = eval(response.choices[0].message.content)

    for i, b in enumerate(bullets):
        b["text"] = rewritten_texts[i]

    return bullets
