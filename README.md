# AI Resume Tailor

AI-powered resume generation system that dynamically tailors resume content to a job description using semantic search and vector embeddings.

---

## 🚀 Overview

AI Resume Tailor ingests a job description and generates a customized resume by:

1. Embedding the job description using AI
2. Comparing it against stored experience bullets in PostgreSQL (pgvector)
3. Ranking the most relevant experience
4. Structuring the content into a professional resume format
5. Rendering the result as a PDF

---

## 🧠 Key Features

- Semantic bullet matching using vector embeddings (pgvector)
- AI-ready architecture with pluggable embedding provider
- Structured resume generation (role + company grouping)
- HTML templating with Jinja2
- PDF generation via wkhtmltopdf
- FastAPI endpoint for resume generation
- Dockerized for full-stack execution

---

## 🏗️ Architecture

Job Description
↓
Embedding (OpenAI / fallback)
↓
PostgreSQL (pgvector)
↓
Similarity Ranking
↓
Resume Builder
↓
HTML Template (Jinja2)
↓
PDF Output

---

## 📂 Project Structure

ai-resume-tailor/
├── app/                  # FastAPI app
├── domain/               # Business logic (pipeline, scoring, builder)
├── infrastructure/       # DB, embeddings, PDF rendering
├── scripts/              # CLI scripts (pipeline, backfill)
├── templates/            # HTML templates
├── docker/               # Dockerfiles
├── docker-compose.yml
└── requirements.txt

---

## ⚙️ Setup (Local)

### 1. Create virtual environment

python -m venv .venv
.venv\Scripts\activate   # Windows

### 2. Install dependencies

pip install -r requirements.txt

### 3. Set environment variables

Create `.env`:

DATABASE_URL=postgresql://resume:resume@localhost:5432/resume
USE_OPENAI=false

---

## 🧪 Run Pipeline (CLI)

python -m scripts.run_pipeline

Output:
resume.pdf

---

## 🌐 Run API

uvicorn app.main:app --reload

Open:
http://127.0.0.1:8000/docs

---

## 📬 API Usage

POST /generate-resume

Example:

curl -X POST "http://localhost:8000/generate-resume" \
  -F "file=@sample_job.txt" \
  --output resume.pdf

---

## 🐳 Docker Setup

docker compose up --build

---

## 🧠 Embeddings

Supports:

- OpenAI (text-embedding-3-small)
- Local fallback (for development)

Enable OpenAI:

set USE_OPENAI=true
set OPENAI_API_KEY=your_key

---

## 🗄️ Database

- PostgreSQL
- pgvector extension

Core table:
resume_domain.experience_bullet

Includes:
- bullet_text
- embedding (vector)

---

## 🔥 Future Enhancements

- AI-powered bullet rewriting
- Resume summary generation
- Multiple resume templates/styles
- Frontend UI
- Async job processing
- Resume history storage

---

## 🎯 Why This Project Matters

This project demonstrates:

- Data engineering + AI integration
- Vector databases (pgvector)
- Backend API design
- Document generation pipelines
- Containerized system architecture

---

## 👤 Author

Jesse Brandon
