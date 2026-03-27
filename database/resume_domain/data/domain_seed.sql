--liquibase formatted sql
--changeset jesse:domain_seed_001 context:local
-- Employer
INSERT INTO resume_domain.employer (employer_id, employer_name, location)
VALUES (
        'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa',
        'Sherwin Williams',
        'Spartanburg, SC'
    );
-- Role
INSERT INTO resume_domain.role (
        role_id,
        employer_id,
        role_title,
        start_date,
        end_date
    )
VALUES (
        'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb',
        'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa',
        'Senior SQL Developer',
        '2020-01-01',
        '2023-01-01'
    );
-- Bullets
INSERT INTO resume_domain.experience_bullet (
        bullet_id,
        role_id,
        bullet_text,
        impact_score
    )
VALUES (
        'c1111111-1111-1111-1111-111111111111',
        'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb',
        'Optimized SQL queries reducing execution time by 80%',
        5
    ),
    (
        'c2222222-2222-2222-2222-222222222222',
        'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb',
        'Designed star schema data warehouse for analytics',
        5
    );
-- Skills
INSERT INTO resume_domain.skill (skill_id, skill_name)
VALUES (
        '11111111-1111-1111-1111-111111111111',
        'PostgreSQL'
    ),
    ('22222222-2222-2222-2222-222222222222', 'Python'),
    (
        '33333333-3333-3333-3333-333333333333',
        'Terraform'
    );
-- Bullet ↔ Skill
INSERT INTO resume_domain.bullet_skill (bullet_id, skill_id)
VALUES (
        'c1111111-1111-1111-1111-111111111111',
        '11111111-1111-1111-1111-111111111111'
    ),
    (
        'c2222222-2222-2222-2222-222222222222',
        '11111111-1111-1111-1111-111111111111'
    );
