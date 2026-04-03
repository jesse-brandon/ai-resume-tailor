--liquibase formatted sql
--changeset jesse-brandon:profile_001 labels:table
CREATE TABLE resume_domain.profile (
    profile_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    full_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT,
    location TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);
--changeset jesse-brandon:profile_002 labels:index
CREATE UNIQUE INDEX one_active_profile ON resume_domain.profile (is_active)
WHERE is_active = TRUE;
