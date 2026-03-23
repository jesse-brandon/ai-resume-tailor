from infrastructure.db.connection import get_connection


def fetch_all_bullets():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT bullet_id, bullet_text
        FROM resume_domain.experience_bullet
    """
    )

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [{"id": r[0], "text": r[1]} for r in rows]
