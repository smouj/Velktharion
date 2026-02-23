# Release Process

## Versioning
- Semantic Versioning: `MAJOR.MINOR.PATCH`

## Steps
1. Update docs + changelog
2. Ensure CI green
3. Create and push tag: `git tag vX.Y.Z && git push origin vX.Y.Z`
4. GitHub Actions creates release notes automatically
5. Announce release summary in README or discussions

## Rollback
- Re-deploy previous known-good tag
- Open postmortem issue if rollback was needed
