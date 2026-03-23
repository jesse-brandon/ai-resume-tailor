# AI Resume Tailor — ER Diagram

```mermaid
erDiagram

    %% ========================
    %% resume_raw
    %% ========================

    resume_raw_job_description {
        UUID job_id PK
        TEXT company_name
        TEXT role_title
        TEXT source
        TIMESTAMP created_at
    }

    resume_raw_document_text {
        UUID document_id PK
        TEXT extracted_text
    }

    %% ========================
    %% resume_domain
    %% ========================

    resume_domain_employer {
        UUID employer_id PK
        TEXT employer_name
    }

    resume_domain_role {
        UUID role_id PK
        UUID employer_id FK
        TEXT role_title
        DATE start_date
        DATE end_date
    }

    resume_domain_experience_bullet {
        UUID bullet_id PK
        UUID role_id FK
        TEXT bullet_text
        INTEGER impact_score
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    resume_domain_skill {
        UUID skill_id PK
        TEXT skill_name
    }

    resume_domain_bullet_skill {
        UUID bullet_id FK
        UUID skill_id FK
    }

    %% ========================
    %% resume_ai
    %% ========================

    resume_ai_job_keyword {
        UUID keyword_id PK
        UUID job_id FK
        TEXT keyword
        NUMERIC weight
    }

    resume_ai_bullet_score {
        UUID job_id FK
        UUID bullet_id FK
        NUMERIC score
        TEXT reasoning
    }

    resume_ai_scoring_run {
        UUID run_id PK
        UUID job_id FK
        TEXT model_name
        TIMESTAMP created_at
    }

    resume_ai_bullet_embedding {
        UUID bullet_id FK
        TEXT model_name
        VECTOR embedding
    }

    resume_ai_job_embedding {
        UUID job_id FK
        TEXT model_name
        VECTOR embedding
    }

    %% ========================
    %% resume_build
    %% ========================

    resume_build_resume {
        UUID resume_id PK
        UUID job_id FK
        TEXT template_name
        TIMESTAMP created_at
        TEXT pdf_location
    }

    resume_build_resume_section {
        UUID section_id PK
        UUID resume_id FK
        TEXT section_name
        INTEGER section_order
    }

    resume_build_resume_bullet {
        UUID section_id FK
        UUID bullet_id FK
        INTEGER bullet_order
    }

    %% ========================
    %% resume_admin
    %% ========================

    resume_admin_pipeline_run {
        UUID run_id PK
        UUID job_id FK
        TEXT status
        TIMESTAMP start_time
        TIMESTAMP end_time
        TIMESTAMP created_at
    }

    %% ========================
    %% RELATIONSHIPS
    %% ========================

    resume_domain_employer ||--o{ resume_domain_role : employs
    resume_domain_role ||--o{ resume_domain_experience_bullet : has

    resume_domain_experience_bullet ||--o{ resume_domain_bullet_skill : maps
    resume_domain_skill ||--o{ resume_domain_bullet_skill : maps

    resume_raw_job_description ||--o{ resume_ai_job_keyword : has
    resume_raw_job_description ||--o{ resume_ai_bullet_score : evaluated_against
    resume_domain_experience_bullet ||--o{ resume_ai_bullet_score : scored

    resume_raw_job_description ||--|| resume_ai_job_embedding : embedded
    resume_domain_experience_bullet ||--|| resume_ai_bullet_embedding : embedded

    resume_raw_job_description ||--o{ resume_build_resume : generates

    resume_build_resume ||--o{ resume_build_resume_section : contains
    resume_build_resume_section ||--o{ resume_build_resume_bullet : contains
    resume_domain_experience_bullet ||--o{ resume_build_resume_bullet : selected

    resume_raw_job_description ||--o{ resume_admin_pipeline_run : processed
```

---

# Diagram Notes

## Core Flow

```text
Job → Keywords + Embedding → Bullet Scoring → Resume Build
```

---

## Key Relationships

### Career Data

* Employer → Role → Experience Bullet
* Bullet ↔ Skill (many-to-many)

---

### AI Layer

* Job → Keywords
* Job ↔ Bullet → Score
* Job → Embedding
* Bullet → Embedding

---

### Resume Construction

```text
Resume
   ↓
Sections
   ↓
Bullets (selected from experience)
```

---

### Pipeline Tracking

* Each job processed creates a `pipeline_run`
