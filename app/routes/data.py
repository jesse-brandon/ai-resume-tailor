from uuid import UUID

from fastapi import APIRouter
from pydantic import BaseModel

from infrastructure.db.connection import get_connection
from infrastructure.embeddings.provider import embed_text

router = APIRouter(prefix="/data", tags=["data"])


class EmployerCreate(BaseModel):
    employer_name: str


class RoleCreate(BaseModel):
    employer_id: UUID
    role_title: str


class SkillCreate(BaseModel):
    skill_name: str


class BulletCreate(BaseModel):
    role_id: UUID
    bullet_text: str


class BulletSkillCreate(BaseModel):
    bullet_id: UUID
    skill_id: UUID


@router.post("/employers")
def create_employer(payload: EmployerCreate):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO resume_domain.employer (employer_name)
        VALUES (%s)
        RETURNING employer_id
    """,
        (payload.employer_name,),
    )

    employer_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return {"employer_id": str(employer_id)}


@router.post("/roles")
def create_role(payload: RoleCreate):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO resume_domain.role (employer_id, role_title)
        VALUES (%s, %s)
        RETURNING role_id
    """,
        (payload.employer_id, payload.role_title),
    )

    role_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return {"role_id": str(role_id)}


@router.post("/skills")
def create_skill(payload: SkillCreate):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO resume_domain.skill (skill_name)
        VALUES (%s)
        RETURNING skill_id
    """,
        (payload.skill_name,),
    )

    skill_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return {"skill_id": str(skill_id)}


from infrastructure.embeddings.provider import embed_text


@router.post("/bullets")
def create_bullet(payload: BulletCreate):

    conn = get_connection()
    cur = conn.cursor()

    embedding = embed_text(payload.bullet_text)

    cur.execute(
        """
        INSERT INTO resume_domain.experience_bullet (role_id, bullet_text, embedding)
        VALUES (%s, %s, %s)
        RETURNING bullet_id
    """,
        (payload.role_id, payload.bullet_text, embedding),
    )

    bullet_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return {"bullet_id": str(bullet_id)}


@router.get("/bullets")
def get_bullets():

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


@router.post("/bullet-skills")
def link_bullet_skill(payload: BulletSkillCreate):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO resume_domain.bullet_skill (bullet_id, skill_id)
        VALUES (%s, %s)
    """,
        (payload.bullet_id, payload.skill_id),
    )

    conn.commit()
    cur.close()
    conn.close()

    return {"status": "linked"}
