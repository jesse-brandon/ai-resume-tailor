import json
import os

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def rewrite_bullets(bullets: list, job_description: str) -> list:

    if not bullets:
        return bullets

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
    try:
        response = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[{"role": "user", "content": prompt}],
        )

        response_text = response.choices[0].message.content or ""

        rewritten_texts = json.loads(response_text)

        # ✅ Validate length matches
        if len(rewritten_texts) != len(bullets):
            raise ValueError("Mismatch in bullet count")

        # ✅ Apply rewritten bullets
        for i, b in enumerate(bullets):
            b["text"] = rewritten_texts[i]

        return bullets

    except Exception as e:
        print("⚠️ AI rewrite failed — using original bullets")
        print("ERROR:", e)

        # 🔥 Fallback: return ORIGINAL bullets unchanged
        return bullets
