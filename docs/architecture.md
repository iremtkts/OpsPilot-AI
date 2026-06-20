# System Architecture

## Main Layers

### API Layer

Defines HTTP endpoints, authentication entry points, request context, dependency wiring, and transport-level error responses. It delegates business behavior rather than implementing it.

### Schema Layer

Defines validated request, response, event, and internal data-transfer contracts. Schemas keep transport models separate from persistence models.

### Service Layer

Coordinates use cases, authorization decisions, transactions, and interactions among repositories, workflows, retrieval, LLMs, and integrations.

### Repository Layer

Provides persistence interfaces for relational data and hides database-specific query details from services.

### RAG Layer

Owns document ingestion, sanitization, chunking, embeddings, vector indexing, retrieval, reranking, context filtering, and citations.

### LLM Gateway

Provides a provider-agnostic interface for model capabilities, token budgets, retries, timeouts, privacy policy, structured output, and usage metadata.

### Workflow Engine

Executes deterministic and AI-assisted steps with durable state, idempotency, retry policies, deadlines, and approval checkpoints.

### Agent Layer

Hosts bounded, task-specific agents. Agents receive only approved tools and context, and cannot bypass authorization or human approval policies.

### Integrations Layer

Encapsulates GitHub, Google Sheets, Apps Script, object storage, and future external APIs. Each adapter handles provider authentication, rate limits, errors, and data mapping.

### Privacy and Security Layer

Centralizes identity context, authorization, organization separation, PII and secret detection, redaction, prompt safety, action policies, encryption expectations, and audit events.

### Observability Layer

Produces structured logs, metrics, traces, audit records, correlation identifiers, model usage, workflow status, and sanitized diagnostic context.

## High-Level System Flow

```text
Clients / Future Dashboard
          |
          v
      API Layer
          |
          v
  Application Services
    /      |       \
   v       v        v
 RAG   Workflow   Integrations
   \       |        /
    v      v       v
       LLM Gateway
           |
           v
 Local or Hosted LLM Providers

Services <-> Repositories <-> PostgreSQL
RAG      <-> Vector Store / Object Storage
All layers -> Privacy, Security, Observability, Audit
External writes -> Policy Check -> Human Approval -> Integration
```

## Boundary and Extraction Strategy

The first deployment may share a process and database, but modules must own their contracts and data access. Background ingestion, scheduled jobs, or workflow execution may run through separate process entry points while reusing the same domain modules. Candidate modules should be separated only when evidence shows a need for independent scaling, fault isolation, compliance boundaries, or team ownership.

## Agent Architecture Direction

The first agent capability will use a controlled single planner agent. It will operate within a bounded workflow, receive an explicit tool allowlist, produce inspectable plans, and route consequential external actions through policy checks and human approval.

The platform may later evolve toward a multi-agent architecture when specialization provides measurable value:

- **Retrieval Agent:** gathers authorized evidence and returns citation-ready context.
- **GitHub Analysis Agent:** interprets repository, pull request, issue, and delivery signals.
- **Workflow Agent:** coordinates deterministic and model-assisted operational steps.
- **Feedback Triage Agent:** classifies feedback, identifies urgency, and proposes routing.
- **Approval/Safety Agent:** evaluates proposed actions against policy and prepares human-readable approval context.

Specialized agents will not receive unrestricted peer-to-peer autonomy. A shared workflow state, tool contracts, authorization checks, trace data, execution limits, and approval gates will keep orchestration controlled and auditable. LangGraph is a future implementation option for this stateful orchestration, not a dependency of the initial backend foundation.

## Production Concerns

- **Testability:** dependency inversion, deterministic service tests, integration tests for infrastructure adapters, and contract tests for providers
- **Observability:** correlation IDs, structured logs, metrics, traces, model usage, workflow state, and actionable alerts
- **Security:** least privilege, validated input, dependency management, secure defaults, protected secrets, and audited external actions
- **Privacy:** redaction, provider policy, scoped retrieval, sanitized diagnostics, retention rules, and deletion support
- **Deployment readiness:** immutable artifacts, automated checks, environment-based configuration, health probes, rollback, and scale-to-zero support
- **Maintainability:** typed interfaces, cohesive modules, migrations, ADRs, concise documentation, and controlled dependency direction

The architecture favors dependable boundaries over premature distribution.
