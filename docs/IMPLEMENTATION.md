# Implementation Guide — Velktharion

## Objective
Build a reliable, local-first skill for: **Autonomous browser with persistent memory**.

## Engineering principles
1. Deterministic behavior over hidden magic
2. Typed interfaces and explicit contracts
3. Replayable traces for debugging
4. Policy gates for sensitive actions
5. Test-first for critical logic paths

## Phased implementation

### Phase 1 — Core skeleton
- Define `SkillConfig`, `TaskInput`, `TaskResult`
- Implement baseline orchestrator in `core/orchestrator.py`
- Add CLI entrypoint with dry-run mode

### Phase 2 — Tool adapters
- Add adapters for external integrations
- Normalize I/O in pydantic schemas
- Add retry/backoff policy with tenacity

### Phase 3 — Memory and context
- Implement short-term run context
- Add optional persistent store adapter
- Add citation/trace references

### Phase 4 — Safety and reliability
- Add policy checks before side effects
- Add idempotency keys for write operations
- Add structured logs and failure classes

### Phase 5 — Quality gates
- Unit tests for core logic
- Smoke tests for CLI path
- Lint + typecheck + CI baseline
