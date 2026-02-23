# Velktharion

![Language](https://img.shields.io/badge/language-Python%203.11%2B-blue)
![License](https://img.shields.io/github/license/smouj/Velktharion)
![Last Commit](https://img.shields.io/github/last-commit/smouj/Velktharion)
![CI](https://img.shields.io/badge/CI-planned-lightgrey)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-Support%20this%20project-ff5f5f?logo=ko-fi&logoColor=white)](https://ko-fi.com/smouj013_dev)

<p align="center">
  <a href="./README.md"><img src="https://img.shields.io/badge/README-English-1f6feb?style=for-the-badge" alt="English"></a>
  <a href="./README.es.md"><img src="https://img.shields.io/badge/README-Español-c92a2a?style=for-the-badge" alt="Español"></a>
</p>

**Autonomous browser intelligence with persistent strategic memory.**

## Vision
Velktharion is a production-oriented skill in the **smouj SuperAgents Universe**. It is designed to solve a concrete operational problem with local-first execution, transparent reasoning traces, and practical safety controls. The architecture prioritizes free/open-source tooling, deterministic behavior, and modular integration with other autonomous skills.

## Core Superpower
- ⚡ **State-aware autonomous browsing that learns from every run**

## Current Status (February 2026)
- 🚧 Ideation and robust scaffolding phase
- Next milestones:
  - [ ] Finalize domain contracts and interfaces
  - [ ] Ship a minimal runnable CLI command
  - [ ] Add Ollama local model profile and fallback strategy
  - [ ] Implement one complete end-to-end example
  - [ ] Add quality gates (lint, typecheck, test)
  - [ ] Publish architecture and operational runbook

## Planned Architecture (free/open-source stack)
- **Primary language:** Python 3.11+
- **Agent framework:** LangGraph
- **Local models:** Ollama (Llama 3.1, Qwen2.5, DeepSeek-Coder, Mistral)
- **Core dependencies:** playwright, chromadb, pydantic, httpx, tenacity
- **Execution model:** local-first, optional self-hosted deployment

## Capability Blueprint
- ✅ Navigation planning
- ✅ Session memory graph
- ✅ Resilient retries
- ✅ Structured extraction
- ✅ Action safety policies


## Project Structure
```text
Velktharion/
├── src/velktharion/
│   ├── core/           # domain orchestration and policies
│   ├── adapters/       # external integrations and tool bridges
│   ├── memory/         # state, retrieval, and context strategies
│   └── cli.py          # local operator command interface
├── docs/
│   ├── IMPLEMENTATION.md
│   ├── ARCHITECTURE.md
│   └── RUNBOOK.md
├── examples/
├── tests/
├── requirements.txt
└── README.md
```

## Quick Start
```bash
git clone https://github.com/smouj/Velktharion.git
cd Velktharion
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m src.velktharion.cli --help
```

## Documentation
- [Implementation Guide](./docs/IMPLEMENTATION.md)
- [Architecture](./docs/ARCHITECTURE.md)
- [Runbook](./docs/RUNBOOK.md)
- [Deployment Guide](./docs/DEPLOYMENT.md)
- [Release Process](./docs/RELEASE.md)
- [Changelog](./CHANGELOG.md)
- [Contributing](./CONTRIBUTING.md)

## Contributing
Contributions are welcome. Please read **CONTRIBUTING.md** before opening issues or PRs.

## License
MIT © 2026 smouj
