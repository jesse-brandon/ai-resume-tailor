--liquibase formatted sql
--changeset jesse-brandon:bullet_embedding_001 labels:table
CREATE TABLE resume_ai.bullet_embedding (
    bullet_id UUID PRIMARY KEY,
    model_name TEXT,
    embedding vector(1536),
    CONSTRAINT fk_bullet_embedding_bullet FOREIGN KEY (bullet_id) REFERENCES resume_domain.experience_bullet(bullet_id)
);
--changeset jesse-brandon:bullet_embedding_002 labels:index
CREATE INDEX ix_bullet_embedding_vector ON resume_ai.bullet_embedding USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
