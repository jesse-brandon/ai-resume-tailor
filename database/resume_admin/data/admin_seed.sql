--liquibase formatted sql
--changeset jesse:admin_seed_001 contexts:local
INSERT INTO resume_admin.pipeline_run (
        run_id,
        job_id,
        status,
        start_time,
        end_time
    )
VALUES (
        '11111111-1111-1111-1111-111111111111',
        '11111111-1111-1111-1111-111111111111',
        'COMPLETED',
        now(),
        now()
    );
