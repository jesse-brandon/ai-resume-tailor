# AI Resume Tailor — Data Model

## Overview

The **AI Resume Tailor** database is designed to support a fully automated pipeline that:

1. Ingests job descriptions
2. Stores structured career experience
3. Uses AI to score and rank experience
4. Dynamically assembles tailored resumes
5. Tracks pipeline execution

The system follows a **domain-driven schema design** using PostgreSQL and Liquibase.

---

## Schema Architecture

| Schema          | Purpose                                       |
| --------------- | --------------------------------------------- |
| `resume_raw`    | Job ingestion and document parsing            |
| `resume_domain` | Core career data (roles, bullets, skills)     |
| `resume_ai`     | AI processing (embeddings, scoring, keywords) |
| `resume_build`  | Resume assembly and structure                 |
| `resume_admin`  | Pipeline tracking and system metadata         |

---

## End-to-End Data Flow

```
Job Description (resume_raw)
        ↓
Keyword Extraction + Embedding (resume_ai)
        ↓
Bullet Scoring (resume_ai)
        ↓
Resume Assembly (resume_build)
        ↓
Pipeline Tracking (resume_admin)
```

---

# Schema Details

---

## 1. resume_raw

### Purpose

Stores incoming job descriptions and extracted text.

### Tables

#### job_description

| Column       | Type      | Description             |
| ------------ | --------- | ----------------------- |
| job_id       | UUID (PK) | Unique job identifier   |
| company_name | TEXT      | Company name            |
| role_title   | TEXT      | Job title               |
| source       | TEXT      | Source (LinkedIn, etc.) |
| created_at   | TIMESTAMP | Ingestion timestamp     |

---

#### document_text

| Column         | Type      | Description                 |
| -------------- | --------- | --------------------------- |
| document_id    | UUID (PK) | Document identifier         |
| extracted_text | TEXT      | Parsed job description text |

---

## 2. resume_domain

### Purpose

Stores structured career experience.

---

### employer

| Column        | Type      | Description         |
| ------------- | --------- | ------------------- |
| employer_id   | UUID (PK) | Employer identifier |
| employer_name | TEXT      | Company name        |

---

### role

| Column      | Type      | Description         |
| ----------- | --------- | ------------------- |
| role_id     | UUID (PK) | Role identifier     |
| employer_id | UUID (FK) | References employer |
| role_title  | TEXT      | Job title           |
| start_date  | DATE      | Start date          |
| end_date    | DATE      | End date            |

---

### experience_bullet

| Column       | Type      | Description       |
| ------------ | --------- | ----------------- |
| bullet_id    | UUID (PK) | Bullet identifier |
| role_id      | UUID (FK) | References role   |
| bullet_text  | TEXT      | Resume bullet     |
| impact_score | INTEGER   | Manual importance |
| created_at   | TIMESTAMP | Created timestamp |
| updated_at   | TIMESTAMP | Updated timestamp |

---

### skill

| Column     | Type      | Description      |
| ---------- | --------- | ---------------- |
| skill_id   | UUID (PK) | Skill identifier |
| skill_name | TEXT      | Unique skill     |

---

### bullet_skill

| Column    | Type      | Description                  |
| --------- | --------- | ---------------------------- |
| bullet_id | UUID (FK) | References experience_bullet |
| skill_id  | UUID (FK) | References skill             |

---

## 3. resume_ai

### Purpose

Supports AI-driven ranking and semantic matching.

---

### job_keyword

| Column     | Type      | Description                |
| ---------- | --------- | -------------------------- |
| keyword_id | UUID (PK) | Keyword identifier         |
| job_id     | UUID (FK) | References job_description |
| keyword    | TEXT      | Extracted keyword          |
| weight     | NUMERIC   | Importance score           |

---

### bullet_score

| Column    | Type      | Description         |
| --------- | --------- | ------------------- |
| job_id    | UUID (FK) | Job being evaluated |
| bullet_id | UUID (FK) | Experience bullet   |
| score     | NUMERIC   | AI relevance score  |
| reasoning | TEXT      | AI explanation      |

---

### scoring_run

| Column     | Type      | Description            |
| ---------- | --------- | ---------------------- |
| run_id     | UUID (PK) | Scoring run identifier |
| job_id     | UUID (FK) | Associated job         |
| model_name | TEXT      | AI model used          |
| created_at | TIMESTAMP | Run timestamp          |

---

### bullet_embedding

| Column     | Type         | Description                  |
| ---------- | ------------ | ---------------------------- |
| bullet_id  | UUID (FK)    | References experience_bullet |
| model_name | TEXT         | Embedding model              |
| embedding  | VECTOR(1536) | Embedding vector             |

---

### job_embedding

| Column     | Type         | Description                |
| ---------- | ------------ | -------------------------- |
| job_id     | UUID (FK)    | References job_description |
| model_name | TEXT         | Embedding model            |
| embedding  | VECTOR(1536) | Embedding vector           |

---

### Notes

* Uses **pgvector extension**
* Supports **cosine similarity search**
* Enables semantic matching between jobs and experience

---

## 4. resume_build

### Purpose

Constructs tailored resumes dynamically.

---

### resume

| Column        | Type      | Description       |
| ------------- | --------- | ----------------- |
| resume_id     | UUID (PK) | Resume identifier |
| job_id        | UUID (FK) | Target job        |
| template_name | TEXT      | Resume template   |
| created_at    | TIMESTAMP | Build timestamp   |
| pdf_location  | TEXT      | Output file path  |

---

### resume_section

| Column        | Type      | Description                        |
| ------------- | --------- | ---------------------------------- |
| section_id    | UUID (PK) | Section identifier                 |
| resume_id     | UUID (FK) | Parent resume                      |
| section_name  | TEXT      | Section (Experience, Skills, etc.) |
| section_order | INTEGER   | Display order                      |

---

### resume_bullet

| Column       | Type      | Description                  |
| ------------ | --------- | ---------------------------- |
| section_id   | UUID (FK) | References resume_section    |
| bullet_id    | UUID (FK) | References experience_bullet |
| bullet_order | INTEGER   | Order within section         |

---

## 5. resume_admin

### Purpose

Tracks pipeline execution and system behavior.

---

### pipeline_run

| Column     | Type      | Description           |
| ---------- | --------- | --------------------- |
| run_id     | UUID (PK) | Pipeline execution ID |
| job_id     | UUID (FK) | Job processed         |
| status     | TEXT      | Execution status      |
| start_time | TIMESTAMP | Start time            |
| end_time   | TIMESTAMP | End time              |
| created_at | TIMESTAMP | Record timestamp      |

---

# Key Design Principles

---

## 1. Atomic Experience Model

Experience is stored as **independent bullet points**, enabling:

* AI ranking
* Dynamic resume assembly
* Reusability across jobs

---

## 2. Schema Separation

Each schema represents a **stage in the pipeline**, improving:

* maintainability
* scalability
* clarity

---

## 3. AI-Ready Design

The model supports:

* embeddings (`pgvector`)
* keyword extraction
* explainable scoring
* model versioning (`model_name`)

---

## 4. Resume as Data

Resumes are not static documents — they are:

```
data + ranking + assembly
```

---

## 5. Liquibase-First Approach

All schema changes are:

* version-controlled
* repeatable
* environment consistent

---

# Future Enhancements

* Resume templates (`resume_template`)
* Scoring breakdown (semantic vs keyword vs AI)
* Embedding model registry
* Feature store for AI scoring
* A/B testing of ranking strategies

---

# Summary

This data model enables a **fully automated, AI-driven resume generation platform** by combining:

* structured career data
* semantic search
* AI scoring
* dynamic document assembly

It is designed to be:

* extensible
* reproducible
* production-ready
