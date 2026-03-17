--liquibase formatted sql
--changeset jesse-brandon:employer_001 labels:table
CREATE TABLE resume_domain.employer (
    employer_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    employer_name TEXT NOT NULL
);
