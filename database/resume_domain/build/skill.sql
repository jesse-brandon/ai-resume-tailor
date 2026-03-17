--liquibase formatted sql
--changeset jesse-brandon:skill_001 labels:table
CREATE TABLE resume_domain.skill (
    skill_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    skill_name TEXT UNIQUE NOT NULL
);
