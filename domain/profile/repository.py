import uuid

from infrastructure.db.connection import get_connection


def create_profile(profile_data):
    conn = get_connection()
    cur = conn.cursor()

    profile_id = str(uuid.uuid4())

    cur.execute(
        """
        UPDATE resume_domain.profile
        SET is_active = FALSE
    """
    )

    cur.execute(
        """
        INSERT INTO resume_domain.profile (
            profile_id,
            full_name,
            email,
            phone,
            location,
            is_active
        )
        VALUES (%s, %s, %s, %s, %s, %s)
    """,
        (
            profile_id,
            profile_data.full_name,
            profile_data.email,
            profile_data.phone,
            profile_data.location,
            profile_data.is_active,
        ),
    )

    conn.commit()

    cur.close()
    conn.close()

    return {"profile_id": profile_id}


def get_active_profile():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT full_name, email, phone, location
        FROM resume_domain.profile
        WHERE is_active = TRUE
        LIMIT 1
    """
    )

    row = cur.fetchone()

    cur.close()
    conn.close()

    if not row:
        return None

    return {
        "name": row[0],
        "email": row[1],
        "phone": row[2],
        "location": row[3],
    }
