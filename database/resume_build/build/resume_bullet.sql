--liquibase formatted sql
--changeset jesse-brandon:resume__bullet_001 labels:table
CREATE TABLE resume_build.resume_bullet (
    bullet_id UUID,
    section_id UUID,
    bullet_order INTEGER,
    PRIMARY KEY (section_id, bullet_id),
    CONSTRAINT fk_resume_bullet_section FOREIGN KEY (section_id) REFERENCES resume_build.resume_section(section_id)
);
