from collections import defaultdict


def build_resume(scored_bullets):

    grouped = defaultdict(list)

    for item in scored_bullets:
        b = item["achievement"]

        key = (b["employer"], b["role"])
        grouped[key].append(b["text"])

    sections = []

    for (employer, role), bullets in grouped.items():
        sections.append({"company": employer, "role": role, "bullets": bullets})

    return {"name": "Jesse Brandon", "title": "Data Engineer", "sections": sections}
