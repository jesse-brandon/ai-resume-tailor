--liquibase formatted sql
--changeset jesse-brandon:bullet_score_001 labels:table
CREATE TABLE resume_ai.bullet_score (
    job_id UUID,
    bullet_id UUID,
    score NUMERIC,
    reasoning TEXT,
    PRIMARY KEY (job_id, bullet_id),
    CONSTRAINT fk_bullet_score_job FOREIGN KEY (job_id) REFERENCES resume_raw.job_description(job_id),
    CONSTRAINT fk_bullet_score_bullet FOREIGN KEY (bullet_id) REFERENCES resume_domain.experience_bullet(bullet_id)
);
