--liquibase formatted sql
--changeset jesse-brandon:extensions_001 labels:table
CREATE EXTENSION IF NOT EXISTS pgcrypto;
