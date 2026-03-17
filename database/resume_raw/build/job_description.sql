--liquibase formatted sql
--changeset jesse-brandon:job_description_001 labels:table
CREATE TABLE resume_raw.job_description (
    job_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    company_name TEXT,
    role_title TEXT,
    source TEXT,
    created_at TIMESTAMP DEFAULT now()
);
