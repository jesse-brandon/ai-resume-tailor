--liquibase formatted sql
--changeset jesse-brandon:role_001 labels:table
CREATE TABLE resume_domain.role (
    role_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    employer_id UUID,
    role_title TEXT,
    start_date DATE,
    end_date DATE,
    CONSTRAINT fk_role_employer FOREIGN KEY (employer_id) REFERENCES resume_domain.employer(employer_id)
);
