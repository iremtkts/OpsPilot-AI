# Development Workflow

## Branch Strategy

```text
master
develop
feature/*
docs/*
infra/*
ci/*
fix/*
test/*
chore/*
security/*
```

- `master` is the stable branch and source for the public demonstration deployment.
- `develop` is the integration branch for completed, reviewed work.
- `feature/*` branches are created from `develop` for product capabilities.
- `docs/*` branches contain documentation and architecture decisions.
- `chore/*` branches contain project tooling and maintenance.
- `infra/*` branches contain Docker, cloud, deployment, and infrastructure changes.
- `ci/*` branches contain GitHub Actions and delivery-pipeline changes.
- `fix/*` branches contain defect corrections.
- `test/*` branches improve test coverage or test infrastructure.
- `security/*` branches contain security and privacy changes.

Short-lived branches should be narrowly scoped and merged through reviewed pull requests. Emergency fixes to `master` must be reconciled back into `develop`.

## Initial Branch Sequence

```text
1. docs/architecture-foundation
   Purpose: product, architecture and engineering decisions

2. chore/python-project-bootstrap
   Purpose: create pyproject.toml, uv.lock, .python-version, .env.example,
            .gitignore, Makefile and pre-commit config

3. feature/backend-foundation
   Purpose: create FastAPI app foundation and health/readiness/version endpoints

4. infra/docker-local-runtime
   Purpose: add Dockerfile and Docker Compose for local API runtime

5. ci/backend-quality-gate
   Purpose: add GitHub Actions CI for ruff, mypy, pytest and Docker build
```

Each branch starts from the updated `develop` branch after the preceding branch is reviewed and merged. This sequence separates project tooling, application code, runtime infrastructure, and CI into reviewable changes.

## Python Project Bootstrap Plan

The `chore/python-project-bootstrap` branch will introduce uv, `pyproject.toml`, `uv.lock`, `.python-version`, a uv-managed `.venv`, environment templates, Git ignore rules, a Makefile, and pre-commit configuration. Developers will use `uv sync` to create or synchronize the environment and `uv run` to execute project commands.

Runtime dependencies for the backend foundation:

```bash
uv add fastapi
uv add "uvicorn[standard]"
uv add pydantic
uv add pydantic-settings
uv add structlog
```

Development dependencies:

```bash
uv add --dev pytest
uv add --dev pytest-cov
uv add --dev httpx
uv add --dev ruff
uv add --dev mypy
uv add --dev pre-commit
```

Later database dependencies:

```bash
uv add sqlalchemy
uv add alembic
uv add asyncpg
```

Later RAG dependencies:

```bash
uv add qdrant-client
uv add pypdf
uv add markdown-it-py
uv add tiktoken
```

Later LLM gateway dependencies:

```bash
uv add openai
uv add google-genai
uv add ollama
```

Later agent dependencies:

```bash
uv add langgraph
uv add langchain-core
```

Dependencies should be added only when their owning capability is implemented. This keeps the lockfile intentional and avoids adopting frameworks before their boundaries are defined.

## Commit Convention

Use an imperative, descriptive subject with one of these prefixes:

- `feat:` product capability
- `fix:` defect correction
- `docs:` documentation-only change
- `test:` test addition or correction
- `refactor:` restructuring without intended behavior change
- `chore:` project tooling or maintenance
- `infra:` container, cloud, or infrastructure change
- `ci:` continuous integration or deployment change
- `security:` security or privacy hardening

Examples:

```text
docs: define controlled agent architecture
chore: bootstrap Python project with uv
security: redact provider credentials from structured logs
```

## Pull Request Checklist

- [ ] The change has a focused purpose and targets the correct base branch.
- [ ] The description explains scope, validation, and important trade-offs.
- [ ] Tests cover new or changed behavior.
- [ ] `ruff`, `mypy`, and `pytest` pass where application code exists.
- [ ] Documentation and ADRs are updated when behavior or decisions change.
- [ ] No secrets, credentials, raw sensitive data, or local environment files are included.
- [ ] Security, privacy, migration, observability, and cost impacts were considered.
- [ ] New dependencies are necessary, pinned through uv, and reflected in `uv.lock`.
- [ ] Screenshots, logs, and examples are sanitized.
- [ ] Rollback or recovery considerations are documented when relevant.

## Definition of Done

A future branch is ready to merge when:

- [ ] Tests pass.
- [ ] `ruff` passes.
- [ ] `mypy` passes.
- [ ] Documentation is updated when needed.
- [ ] No secrets are committed.
- [ ] Commits use meaningful messages.
- [ ] The README is updated when relevant.
- [ ] The pull request checklist is satisfied.
