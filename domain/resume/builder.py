def build_resume(scored_achievements, top_n=5):

    top = scored_achievements[:top_n]

    lines = [a["achievement"]["text"] for a in top]

    return "\n".join(lines)
