# OpsPilot AI

OpsPilot AI is a production-grade AI backend and GenAI platform for internal operations automation. It combines privacy-aware retrieval-augmented generation (RAG), LLMOps practices, provider-agnostic model access, approval-gated agents, workflow orchestration, and API integrations in a cloud-ready architecture.

## Problem Statement

Operational knowledge is often fragmented across documents, source-control systems, spreadsheets, and manual processes. Teams need a secure way to retrieve that knowledge, generate actionable insights, and automate repetitive work without granting an AI system uncontrolled access to external systems or exposing sensitive data to model providers.

## What This Project Is

OpsPilot AI is an engineering portfolio project focused on the backend, GenAI, and cloud foundations required to build dependable AI-enabled internal tools. The platform is designed around clean module boundaries, privacy controls, testing, observability, CI/CD, human approval gates, and cost-aware Google Cloud deployment.


## Core Capabilities

- Document ingestion and citation-backed RAG
- GitHub engineering intelligence
- Configurable workflow automation
- AI agents with human approval for external actions
- Google Sheets and Apps Script integrations
- Provider-agnostic local and hosted LLM access
- Privacy controls for PII, secrets, prompts, and logs
- Operational telemetry, auditability, and cost controls
- A future internal dashboard for operators and reviewers

## Architecture Summary

The platform will begin as a modular monolith. A FastAPI application will expose APIs while isolated application modules handle schemas, services, persistence, retrieval, model access, workflows, agents, integrations, privacy, and observability. Asynchronous or scheduled workloads will run separately from request handling where appropriate.

This structure keeps the first production deployment understandable and economical while preserving boundaries that allow high-load or independently evolving modules to become separate services later.

See:

- [Product Definition](docs/product-definition.md)
- [System Architecture](docs/architecture.md)
- [Cloud Architecture](docs/cloud-architecture.md)
- [Cost-Aware Deployment](docs/cost-aware-deployment.md)
- [Data Privacy](docs/data-privacy.md)
- [Development Workflow](docs/development-workflow.md)

## Planned Technology Stack

| Area | Planned technology |
| --- | --- |
| API | Python, FastAPI, Pydantic |
| Project management | uv, `pyproject.toml`, `uv.lock`, uv-managed `.venv` |
| Data access | SQLAlchemy, Alembic |
| Relational database | PostgreSQL |
| Vector search | Qdrant behind an abstraction |
| Cache and coordination | Redis |
| LLM access | Provider-agnostic gateway, including Ollama local mode |
| Object storage | Google Cloud Storage in cloud environments |
| Local environment | Docker Compose |
| Cloud runtime | Google Cloud Run and Cloud Run Jobs |
| CI/CD | GitHub Actions with Workload Identity Federation |
| Agent orchestration | LangGraph later, with limited LangChain components |
| Quality | pytest, ruff, mypy, pre-commit |
| Observability | Structured logs, metrics, traces, audit events |

The stack is planned rather than implemented and may evolve through documented architecture decisions.

## Development Status

**Phase 1 — Backend foundation**

The repository now includes the initial FastAPI application factory, environment-based
settings, structured logging, and system health endpoints. Database, RAG, LLM,
agent, workflow, integration, and cloud runtime implementations remain future work.

## Backend Foundation

Synchronize the Python 3.12 environment:

```bash
uv sync
```

Run the development API:

```bash
uv run uvicorn app.main:app --reload
```

Available endpoints:

- `GET /health` — application liveness
- `GET /ready` — application readiness and dependency checks
- `GET /version` — service version and environment

Run tests:

```bash
uv run pytest
```

Run all quality checks:

```bash
make quality
```

## Docker Runtime

Build and run the local API container:

```bash
docker compose up --build
```

Validate the running service:

```bash
curl http://localhost:8000/health
curl http://localhost:8000/ready
curl http://localhost:8000/version
```

## Roadmap

1. Architecture and product foundation
2. Python project bootstrap with uv and quality tooling
3. FastAPI backend foundation
4. Local Docker runtime and CI quality gates
5. Persistence, authentication, organization boundaries, and audit foundations
6. Privacy-aware document ingestion and RAG
7. LLM gateway and provider integrations
8. GitHub and Google Sheets integrations
9. Controlled agent workflows and approval gates
10. Observability, security hardening, cloud deployment, and internal dashboard
