def score_achievements(bullets, job_text):

    job_words = set(job_text.lower().split())

    scored = []

    for b in bullets:
        bullet_words = set(b["text"].lower().split())

        score = len(bullet_words & job_words)

        scored.append({"achievement": b, "score": score})

    return sorted(scored, key=lambda x: x["score"], reverse=True)
