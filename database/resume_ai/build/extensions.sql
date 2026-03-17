--liquibase formatted sql
--changeset jesse-brandon:extensions_001 labels:extension
CREATE EXTENSION IF NOT EXISTS vector;
