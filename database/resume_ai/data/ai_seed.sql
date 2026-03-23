--liquibase formatted sql
--changeset jesse:ai_seed_001 contexts:local
-- Keywords
INSERT INTO resume_ai.job_keyword (keyword_id, job_id, keyword, weight)
VALUES (
        '11111111-1111-1111-1111-111111111111',
        '11111111-1111-1111-1111-111111111111',
        'PostgreSQL',
        0.9
    ),
    (
        '22222222-2222-2222-2222-222222222222',
        '11111111-1111-1111-1111-111111111111',
        'ETL',
        0.8
    );
-- Scoring run
INSERT INTO resume_ai.scoring_run (run_id, job_id, model_name)
VALUES (
        '11111111-1111-1111-1111-111111111111',
        '11111111-1111-1111-1111-111111111111',
        'gpt-4o'
    );
-- Bullet scores
INSERT INTO resume_ai.bullet_score (job_id, bullet_id, score, reasoning)
VALUES (
        '11111111-1111-1111-1111-111111111111',
        'c1111111-1111-1111-1111-111111111111',
        0.95,
        'Strong match on SQL optimization'
    ),
    (
        '11111111-1111-1111-1111-111111111111',
        'c2222222-2222-2222-2222-222222222222',
        0.90,
        'Relevant data modeling experience'
    );
