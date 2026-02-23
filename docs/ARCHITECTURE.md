# Architecture — Velktharion

## High-level components
- **Core**: orchestration, policies, decision flow
- **Adapters**: external systems and tools
- **Memory**: context and retrieval strategies
- **CLI**: operator interface

## Data flow
1. Input enters via CLI or API
2. Core validates and plans execution
3. Adapters perform tool operations
4. Memory stores outcome and context
5. Result returns with trace metadata

## Reliability design
- Retry policy for transient failures
- Deterministic serialization for reproducibility
- Explicit error taxonomy
- Safe defaults for destructive paths
