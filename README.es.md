# Velktharion

<p align="center">
  <img src="./assets/branding/logo.svg" alt="Logo de Velktharion" width="88" />
</p>

![Language](https://img.shields.io/badge/language-Python%203.11%2B-blue)
![License](https://img.shields.io/github/license/smouj/Velktharion)
![Last Commit](https://img.shields.io/github/last-commit/smouj/Velktharion)
![CI](https://img.shields.io/github/actions/workflow/status/smouj/Velktharion/ci.yml?branch=main)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-Support%20this%20project-ff5f5f?logo=ko-fi&logoColor=white)](https://ko-fi.com/smouj013_dev)

<p align="center">
  <a href="./README.md"><img src="https://img.shields.io/badge/README-English-1f6feb?style=for-the-badge" alt="English"></a>
  <a href="./README.es.md"><img src="https://img.shields.io/badge/README-Español-c92a2a?style=for-the-badge" alt="Español"></a>
</p>

**Autonomous browser intelligence for resilient web execution.**

## Visión
Executes intent-driven browser tasks with resilient navigation, extraction, and snapshots.

## Problema que resuelve
Web automation breaks when pages change and selectors become unstable.

## Superpoder principal
- ⚡ **Self-healing browser workflows with persistent execution memory**

## Casos de uso clave
- ✅ Automated data collection
- ✅ Form workflows
- ✅ Visual page capture
- ✅ Repeatable UI operations


## Superficie API
`POST /navigate`, `POST /extract`, `POST /snapshot`, `GET /health`

## Stack técnico
- **Stack base:** FastAPI + Playwright + local persistence
- **Ejecución:** local-first, apto para self-hosting
- **Infra:** compatibilidad con Docker Compose + Caddy + Redis/Chroma/Ollama

## Estado actual (Feb 2026)
- ✅ Scaffold público disponible
- ✅ README bilingüe (EN por defecto + ES)
- ✅ Base de CI + release configurada
- 🚧 Endurecimiento de funcionalidades en progreso

## Inicio rápido
```bash
git clone https://github.com/smouj/Velktharion.git
cd Velktharion
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m src.velktharion.cli --help
```

## Documentación
- [Guía de implementación](./docs/IMPLEMENTATION.md)
- [Arquitectura](./docs/ARCHITECTURE.md)
- [Runbook](./docs/RUNBOOK.md)
- [Guía de despliegue](./docs/DEPLOYMENT.md)
- [Proceso de releases](./docs/RELEASE.md)
- [Changelog](./CHANGELOG.md)

## Contribución
Las contribuciones son bienvenidas. Lee [CONTRIBUTING.md](./CONTRIBUTING.md).

## Licencia
MIT © 2026 smouj

---

### Otras skills
Explora el ecosistema completo aquí: **[smouj/smouj](https://github.com/smouj/smouj)**

**Firma:** [@Smouj013](https://x.com/smouj013)
