# Product Definition

## Product Vision

OpsPilot AI will provide a secure, observable, and extensible AI automation layer for internal operations. It should help teams find trusted knowledge, interpret engineering and operational signals, and execute repeatable workflows while keeping people in control of consequential actions.

## Target Users

- Engineering and platform teams reviewing repositories, delivery signals, and operational work
- Operations teams working across documents, spreadsheets, and repeatable processes
- Internal support and knowledge teams that need citation-backed answers
- Technical leaders evaluating safe, production-grade adoption of GenAI
- Developers extending the platform with new integrations, workflows, and model providers

## Problem Statement

Internal work is distributed across disconnected systems and frequently depends on manual lookup, copy-and-paste coordination, or undocumented judgment. Generic AI assistants may improve individual tasks, but often lack organization-specific retrieval, access controls, auditability, predictable integrations, and safeguards around sensitive data and external actions.

OpsPilot AI addresses this gap with a backend platform that treats retrieval, privacy, approval, observability, and deployment as first-class product requirements.

## Core Use Cases

### Document-Based RAG Assistant

Ingest permitted internal documents, retrieve relevant passages, and answer questions with source citations. The pipeline will sanitize sensitive content, preserve access-control metadata, and make uncertainty visible.

### GitHub Engineering Intelligence

Summarize repository activity, pull requests, issues, and delivery signals; identify work that needs attention; and prepare recommendations without silently changing repository state.

### Workflow Automation Engine

Define repeatable, inspectable workflows that combine deterministic steps, retrieval, LLM decisions, integrations, retries, and approval checkpoints.

### AI Agent Layer

Use task-focused agents to plan and assist with multi-step operational work. Read-only tools may be automated within policy; external state changes require explicit authorization and a human approval gate.

### Google Sheets and Apps Script Automation

Read structured operational data, prepare summaries or proposed updates, and coordinate approved changes with Google Sheets and Apps Script workflows.

### Internal Dashboard Later

Add an operator-facing dashboard after the backend contracts stabilize. It will surface runs, approvals, sources, costs, errors, and audit history rather than becoming the primary system boundary.

## Main Product Capabilities

- Multi-source knowledge ingestion and retrieval
- Citation-backed generation and traceable evidence
- Swappable local and hosted LLM providers
- Organization, user, and document-level authorization
- Privacy-aware prompt construction and logging
- Durable workflow state, retries, and idempotent operations
- Human review of proposed external actions
- GitHub and Google workspace integrations
- Audit events, metrics, traces, and usage accounting
- Cost and token budget enforcement

## Success Criteria

- Answers are grounded in authorized sources and include useful citations.
- Sensitive content is detected and handled before data reaches external LLMs.
- Organization and document boundaries are enforced during ingestion and retrieval.
- Every external action is attributable, policy-checked, and approval-gated where required.
- Providers and infrastructure can be changed behind stable application interfaces.
- Core flows are covered by automated tests and observable in local and cloud environments.
- A new developer can run the documented local environment without cloud credentials.
- A demonstration deployment can operate within explicit cloud and LLM cost budgets.
- Architecture decisions and operational trade-offs remain documented as the system evolves.
