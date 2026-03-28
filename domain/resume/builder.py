from collections import defaultdict
from datetime import date


def format_date(value):
    if value is None:
        return "Present"
    if isinstance(value, date):
        return value.strftime("%b %Y")
    return str(value)


def build_resume(scored_bullets):
    grouped = defaultdict(list)

    for item in scored_bullets:
        b = item["achievement"]

        key = (
            b["employer"],
            b["role"],
            b["location"],
            b["start_date"],
            b["end_date"],
        )
        grouped[key].append(b["text"])

    sections = []

    for (employer, role, location, start_date, end_date), bullets in sorted(
        grouped.items(), key=lambda x: x[0][3] if x[0][3] else date.min, reverse=True
    ):
        sections.append(
            {
                "role": role,
                "company": employer,
                "location": location,
                "date_range": f"{format_date(start_date)} - {format_date(end_date)}",
                "bullets": bullets,
            }
        )

    return {
        "name": "Jesse Brandon",
        "title": "Data Engineer",
        "sections": sections,
    }
