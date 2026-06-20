# Cost-Aware Deployment

## Principles

Cost is an architectural constraint, not an afterthought. OpsPilot AI should keep idle infrastructure close to zero, place explicit limits around elastic systems, measure usage, and increase capacity only from observed demand.

- Set Cloud Run minimum instances to `0`.
- Start with low Cloud Run maximum-instance and concurrency limits.
- Do not introduce GKE during the initial phases.
- Do not operate an always-on VM for the API or worker.
- Avoid Cloud SQL initially; use a suitable Neon or Supabase free tier for PostgreSQL.
- Use Qdrant Cloud's free tier or local Qdrant.
- Use Upstash Redis's free tier or local Redis.
- Store cloud objects in Google Cloud Storage with retention and lifecycle rules.
- Control log volume through structured fields, severity thresholds, sampling, exclusions, and retention.
- Enforce file type and upload size limits before storage and processing.
- Set per-request, per-user, and environment-level LLM token and spend budgets.
- Use small, licensed, non-sensitive demonstration datasets.
- Configure Google Cloud billing budgets and threshold alerts.
- Keep secrets in approved secret stores; never hardcode or leak them.
- Prefer bounded Cloud Run Jobs over continuously running workers when workload patterns allow.

Free tiers are useful for development and demonstration, but they are not availability guarantees. Limits and terms must be reviewed before each public deployment.

## Cost Risks

- Runaway LLM loops, oversized context windows, or repeated embedding work
- Unbounded Cloud Run scaling or retries during downstream failures
- Large uploads and duplicate object or vector storage
- High-cardinality, verbose, or sensitive logs
- Database connection exhaustion leading to unnecessary plan upgrades
- Background resources that remain active when no work exists
- CI rebuilding or deploying unchanged components
- Free-tier limits changing or being exceeded unexpectedly

## Cost Control Checklist

- [ ] Cloud billing account has budget thresholds and notification recipients.
- [ ] Cloud Run minimum instances are `0`.
- [ ] Cloud Run maximum instances, concurrency, timeouts, CPU, and memory are bounded.
- [ ] Database, Qdrant, Redis, and object-storage quotas are understood.
- [ ] Upload size, document count, and supported file types are limited.
- [ ] LLM model allowlists, token limits, timeouts, retries, and spend caps are configured.
- [ ] Embeddings and retrieval results are reused where safe.
- [ ] Workflow steps have execution, retry, and recursion limits.
- [ ] Logs exclude prompt bodies, document text, tokens, and secrets.
- [ ] Log retention, sampling, and metrics cardinality are reviewed.
- [ ] Storage lifecycle and deletion policies are enabled.
- [ ] Demo datasets are intentionally small and non-sensitive.
- [ ] CI uses caching and deploys only validated, intended revisions.
- [ ] Unused environments and artifacts are periodically removed.
- [ ] No credentials are committed to source control or exposed in build output.
