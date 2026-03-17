--liquibase formatted sql
--changeset jesse-brandon:pipeline_run_001 labels:table
CREATE TABLE resume_admin.pipeline_run (
    run_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    job_id UUID,
    created_at TIMESTAMP DEFAULT NOW(),
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    status TEXT
);
