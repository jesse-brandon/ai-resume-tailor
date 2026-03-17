--liquibase formatted sql
--changeset jesse-brandon:job_keyword_001 labels:table
CREATE TABLE resume_ai.job_keyword (
    keyword_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    job_id UUID NOT NULL,
    keyword TEXT NOT NULL,
    weight NUMERIC,
    CONSTRAINT fk_job_keyword_job FOREIGN KEY (job_id) REFERENCES resume_raw.job_description(job_id)
);
