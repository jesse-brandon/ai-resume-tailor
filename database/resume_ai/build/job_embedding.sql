--liquibase formatted sql
--changeset jesse-brandon:job_embedding_001 labels:table
CREATE TABLE resume_ai.job_embedding (
    job_id UUID PRIMARY KEY,
    embedding vector(1536),
    CONSTRAINT fk_job_embedding_job FOREIGN KEY (job_id) REFERENCES resume_raw.job_description(job_id)
);
