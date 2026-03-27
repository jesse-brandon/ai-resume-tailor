from infrastructure.db.connection import get_connection


def to_vector_str(embedding):
    return "[" + ",".join(str(x) for x in embedding) + "]"


def rank_bullets(job_embedding, top_n=5):

    conn = get_connection()
    cur = conn.cursor()

    vector_str = to_vector_str(job_embedding)

    cur.execute(
        """
        SELECT
            b.bullet_id,
            b.bullet_text,
            r.role_title,
            r.start_date,
            r.end_date,
            e.employer_name,
            e.location
        FROM resume_domain.experience_bullet b
        JOIN resume_domain.role r
            ON b.role_id = r.role_id
        JOIN resume_domain.employer e
            ON r.employer_id = e.employer_id
        ORDER BY b.embedding <-> %s::vector
        LIMIT %s
    """,
        (vector_str, top_n),
    )

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [
        {
            "id": r[0],
            "text": r[1],
            "role": r[2],
            "start_date": r[3],
            "end_date": r[4],
            "employer": r[5],
            "location": r[6],
        }
        for r in rows
    ]
