# Deployment Guide

## Philosophy
This project is **local-first** and free/open-source by default. Production deployment is optional.

## Recommended deployment paths

### 1) Local execution (default)
- Python 3.11+
- Virtual environment
- Run via CLI or internal API adapter

### 2) Containerized self-hosting
- Build lightweight image from Python slim base
- Mount config and state volumes
- Run behind Caddy/Nginx if exposing HTTP

### 3) Free-tier managed options (optional)
- Fly.io (small workers)
- Railway (hobby starter)
- n8n self-hosted integration

## Baseline operational checklist
- [ ] `ruff check .` passes
- [ ] `pytest -q` passes
- [ ] secrets injected via env vars only
- [ ] health probe endpoint or smoke command available
- [ ] rollback version/tag prepared

## Release + Deploy pattern
1. Cut tag `vX.Y.Z`
2. GitHub Release workflow publishes notes/artifacts
3. Deploy specific tag (never floating branch)
4. Validate smoke command and logs
5. Rollback to prior tag if needed
