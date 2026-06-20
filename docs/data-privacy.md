# Data Privacy and AI Safety

## Why Privacy Matters

RAG and LLM systems combine user input, internal documents, retrieved context, model providers, logs, and external tools. A conventional access check at upload time is insufficient: sensitive data can leak through embeddings, prompts, generated output, diagnostics, caches, or cross-organization retrieval. Privacy controls therefore belong throughout the data lifecycle.

## Required Controls

### PII Detection

Inspect uploaded content and user prompts for defined categories of personally identifiable information. Detection results should be policy inputs, not treated as infallible truth.

### Secret and Token Detection

Detect API keys, access tokens, private keys, credentials, and high-risk patterns before storage, logging, embedding, or model calls. Confirmed secrets should be rejected or irreversibly redacted according to policy.

### Redaction Before LLM Calls

Replace sensitive spans with stable typed placeholders before sending content to an external model. Keep any reversible mapping encrypted, narrowly scoped, and only as long as the use case requires.

### Safe Prompt Builder

Construct prompts from typed sections with clear trust boundaries, permitted instructions, sanitized context, output schemas, and token budgets. Product modules should not concatenate arbitrary raw content into provider prompts.

### Prompt Injection Defense

Treat documents, retrieved text, integration responses, and web content as untrusted data rather than instructions. Use instruction hierarchy, context delimiters, tool allowlists, output validation, retrieval filtering, and approval gates. No single defense is sufficient.

### Audit Logs

Record who initiated a request, organization context, source identifiers, policy decisions, model/provider metadata, proposed actions, approvals, and outcomes. Audit records should be append-oriented and access-controlled.

### Safe Operational Logging

Never write raw secrets to logs. LLM-call logs should contain sanitized metadata such as model, latency, token counts, policy result, correlation ID, and error category without exposing prompt bodies, retrieved passages, or generated sensitive content.

### Human Approval for External Actions

Consequential writes must be represented as a proposed action that includes scope, target, parameters, reason, and expiry. An authorized human approves the exact proposal before execution.

### Access Control and Data Separation

Document-level access control must be applied during ingestion, retrieval, citation resolution, and download. Every durable record and vector must carry organization ownership. Queries must enforce organization separation by construction, with tests designed to detect cross-tenant leakage.

### Retention and Deletion

Define retention periods by data class for source files, extracted text, vectors, prompts, outputs, caches, workflow state, and logs. Deletion must propagate to derived chunks, embeddings, indexes, and cached results, with auditable completion and documented backup behavior.

## Privacy-Aware RAG Pipeline

```text
Upload document
-> Validate file type and size
-> Extract text
-> Detect PII/secrets
-> Redact sensitive content
-> Chunk sanitized text
-> Generate embeddings
-> Store vectors and metadata
-> Retrieve context
-> Apply context safety filtering
-> Call LLM
-> Return answer with citations
-> Log sanitized metadata
```

Authorization checks apply before upload, during every retrieval query, and when resolving citations. Sanitization and access-control metadata must remain linked to the document version from which vectors were derived.

## Provider and Data Governance

Each LLM or embedding provider must have a documented policy covering data residency, retention, training use, encryption, subprocessors, and deletion where applicable. Privacy-sensitive workloads should be routable to an approved provider or Ollama local mode. Provider selection must never silently weaken the request's privacy policy.

This document defines engineering direction, not a claim of legal or regulatory compliance. Applicable requirements must be reviewed before processing real organizational or personal data.
