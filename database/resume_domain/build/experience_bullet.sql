--liquibase formatted sql
--changeset jesse-brandon:experience_bullet_001 labels:table
CREATE TABLE resume_domain.experience_bullet (
    bullet_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    role_id UUID,
    bullet_text TEXT NOT NULL,
    impact_score INTEGER,
    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now(),
    CONSTRAINT fk_experience_bullet FOREIGN KEY (role_id) REFERENCES resume_domain.role(role_id)
);
--changeset jesse-brandon:experience_bullet_002 labels:index
CREATE INDEX ix_experience_bullet_role ON resume_domain.experience_bullet(role_id);
