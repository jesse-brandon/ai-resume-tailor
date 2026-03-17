--liquibase formatted sql
--changeset jesse:score_bullets runOnChange:true splitStatements:false
CREATE OR REPLACE FUNCTION resume_ai.score_bullets() RETURNS void AS $$ BEGIN -- scoring logic
SELECT NULL;
END;
$$ LANGUAGE plpgsql;
