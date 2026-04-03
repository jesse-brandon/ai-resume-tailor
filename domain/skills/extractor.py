from collections import Counter


def extract_skills(bullets, job_description, top_n=10):

    skills = []

    for b in bullets:
        skills.extend(b.get("skills", []))

    counts = Counter(skills)

    # Boost skills mentioned in job description
    boosted = {}

    for skill, count in counts.items():
        if skill.lower() in job_description.lower():
            boosted[skill] = count + 5  # boost weight
        else:
            boosted[skill] = count

    return sorted(boosted, key=boosted.get, reverse=True)[:top_n]
