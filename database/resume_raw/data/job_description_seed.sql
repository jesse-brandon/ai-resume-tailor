--liquibase formatted sql
--changeset jesse:job_seed_001 contexts:local
INSERT INTO resume_raw.job_description (job_id, company_name, role_title, source)
VALUES (
        '11111111-1111-1111-1111-111111111111',
        'TechCorp',
        'Data Engineer',
        'LinkedIn'
    );
