# Cloud Architecture

## Deployment Goals

The target architecture prioritizes low idle cost, managed services, secure workload identity, and straightforward operations. Local development remains the default path; cloud resources validate deployment and support public demonstrations without becoming a prerequisite for implementation.

## Target Cloud Flow

```text
GitHub Actions
  -> Artifact Registry
  -> Cloud Run
  -> Neon/Supabase PostgreSQL
  -> Qdrant Cloud
  -> Upstash Redis
  -> Google Cloud Storage
  -> LLM Provider Gateway
  -> Cloud Logging / Cloud Monitoring
```

This diagram represents the delivery path and primary runtime dependencies, not a synchronous request chain. The application accesses each data or provider service according to the use case.

## Service Responsibilities

### Cloud Run

Hosts the stateless API container, scales based on demand, exposes health endpoints, and uses a dedicated least-privilege service account. Minimum instances should be `0` in cost-sensitive environments.

### Cloud Run Jobs

Runs bounded background workloads such as document ingestion, reindexing, maintenance, or scheduled batch processing when they do not fit the request lifecycle.

### Artifact Registry

Stores immutable, versioned container images produced by CI. Deployments should reference traceable image versions rather than mutable local builds.

### Google Cloud Storage

Stores uploaded source documents and generated artifacts with restricted access, retention rules, and lifecycle policies. Database records hold authorization and metadata rather than raw file content.

### Secret Manager

Stores production API keys, credentials, and sensitive configuration. Cloud Run receives only the secrets required by its service identity.

### Cloud Logging

Collects structured, sanitized application and platform logs. Log exclusions, sampling, and retention should prevent sensitive content leakage and uncontrolled cost.

### Cloud Monitoring

Tracks availability, latency, errors, saturation, job outcomes, and selected product metrics. Alerts should be actionable and aligned with the project's service objectives.

### Neon or Supabase PostgreSQL

Provides an external managed PostgreSQL option with a low-cost starting tier. Connection pooling and service limits must be evaluated before production traffic increases.

### Qdrant Cloud

Provides managed vector search with metadata filtering. Local Qdrant remains available for development and as a fallback for demonstrations.

### Upstash Redis

Provides a low-idle-cost managed Redis-compatible service for caching, rate limiting, and short-lived coordination. Redis must not be the only durable workflow store.

### GitHub Actions OIDC and Workload Identity Federation

Allows CI to authenticate to Google Cloud with short-lived credentials. Long-lived GCP service account keys should not be created or stored in GitHub secrets.

## Local-First Strategy

Local development will use containerized PostgreSQL, Qdrant, and Redis, local file or object-storage substitutes, and optional Ollama inference. Environment-specific adapters and configuration will preserve consistent application interfaces without requiring cloud credentials for routine development or tests.

## Initial Constraints

- No Google Kubernetes Engine initially; orchestration overhead is not justified.
- No always-on virtual machine initially; idle capacity conflicts with cost goals.
- No Cloud SQL initially; Neon or Supabase offers a lower-cost validation path.
- Cloud Run minimum instances should remain `0` unless measured latency requirements justify a change.
- Long-lived GCP service account keys should be avoided in favor of workload identity.
- Secrets and local environment files must not be committed to the repository.
- Production data services must enforce encryption, access restrictions, backups, and documented recovery expectations appropriate to their tier.
