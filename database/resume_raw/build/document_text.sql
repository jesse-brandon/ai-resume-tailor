--liquibase formatted sql
--changeset jesse-brandon:document_text_001 labels:table
CREATE TABLE resume_raw.document_text (
    document_id UUID PRIMARY KEY,
    extracted_text TEXT
);
