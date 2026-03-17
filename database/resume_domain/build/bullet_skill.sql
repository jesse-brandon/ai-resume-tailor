--liquibase formatted sql
--changeset jesse-brandon:bullect_skill_001 labels:table
CREATE TABLE resume_domain.bullet_skill (
    bullet_id UUID,
    skill_id UUID,
    PRIMARY KEY (bullet_id, skill_id),
    CONSTRAINT fk_bullet_skill_bullet FOREIGN KEY (bullet_id) REFERENCES resume_domain.experience_bullet(bullet_id),
    CONSTRAINT fk_bullet_skill_skill FOREIGN KEY (skill_id) REFERENCES resume_domain.skill(skill_id)
);
