--liquibase formatted sql
--changeset jesse:build_seed_001 contexts:local
-- Resume
INSERT INTO resume_build.resume (
        resume_id,
        job_id,
        template_name,
        pdf_location
    )
VALUES (
        'd1111111-1111-1111-1111-111111111111',
        '11111111-1111-1111-1111-111111111111',
        'data-engineer',
        '/resumes/sample.pdf'
    );
-- Sections
INSERT INTO resume_build.resume_section (
        section_id,
        resume_id,
        section_name,
        section_order
    )
VALUES (
        'e1111111-1111-1111-1111-111111111111',
        'd1111111-1111-1111-1111-111111111111',
        'Experience',
        1
    );
-- Resume bullets
INSERT INTO resume_build.resume_bullet (section_id, bullet_id, bullet_order)
VALUES (
        'e1111111-1111-1111-1111-111111111111',
        'c1111111-1111-1111-1111-111111111111',
        1
    );
