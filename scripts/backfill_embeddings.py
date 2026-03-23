from infrastructure.db.connection import get_connection
from infrastructure.embeddings.provider import embed_text


def run():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT bullet_id, bullet_text
        FROM resume_domain.experience_bullet
        WHERE embedding IS NULL
    """
    )

    rows = cur.fetchall()

    for bullet_id, text in rows:
        emb = embed_text(text)

        cur.execute(
            """
            UPDATE resume_domain.experience_bullet
            SET embedding = %s
            WHERE bullet_id = %s
        """,
            (emb, bullet_id),
        )

        print(f"Embedded bullet {bullet_id}")

    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    run()
