--liquibase formatted sql
--changeset jesse-brandon:scoring_run_001 labels:table
CREATE TABLE resume_ai.scoring_run (
    run_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    job_id UUID,
    created_at TIMESTAMP DEFAULT now(),
    model_name TEXT,
    CONSTRAINT fk_scoring_run_job FOREIGN KEY (job_id) REFERENCES resume_raw.job_description(job_id)
);
