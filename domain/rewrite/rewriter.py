import json
import os

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def rewrite_bullets(bullets: list, job_description: str) -> list:

    bullet_texts = [b["text"] for b in bullets]

    prompt = f"""
        You are a senior technical resume writer.

        Rewrite each bullet to align with the job description.

        STRICT RULES:
        - Return ONLY valid JSON
        - No explanations
        - No numbering
        - No markdown
        - Output format EXACTLY:
        ["bullet1", "bullet2", ...]

        Job Description:
        {job_description}

        Bullets:
        {bullet_texts}
    """

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    response_text = response.choices[0].message.content or ""

    try:
        rewritten_texts = json.loads(response_text)

        if not isinstance(rewritten_texts, list):
            raise ValueError("Response is not a list")

    except Exception as e:
        print("RAW AI RESPONSE:")
        print(response_text)
        raise Exception(f"Failed to parse AI response: {e}")

    for i, b in enumerate(bullets):
        b["text"] = rewritten_texts[i]

    return bullets
