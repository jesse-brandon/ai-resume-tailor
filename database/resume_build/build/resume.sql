--liquibase formatted sql
--changeset jesse-brandon:resume_001 labels:table
CREATE TABLE resume_build.resume (
    resume_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    job_id UUID,
    created_at TIMESTAMP DEFAULT now(),
    pdf_location TEXT,
    template_name TEXT
);
