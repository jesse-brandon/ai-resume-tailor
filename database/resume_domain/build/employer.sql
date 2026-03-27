--liquibase formatted sql
--changeset jesse-brandon:employer_001 labels:table
CREATE TABLE resume_domain.employer (
    employer_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    employer_name TEXT NOT NULL
);
--changeset jesse-brandon:employer_002 labels:table
ALTER TABLE resume_domain.employer
ADD COLUMN location TEXT NULL;
