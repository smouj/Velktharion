"""CLI entrypoint for Velktharion."""
from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass
class TaskResult:
    ok: bool
    message: str


def run(dry_run: bool = True) -> TaskResult:
    if dry_run:
        return TaskResult(ok=True, message="Dry run executed successfully.")
    return TaskResult(ok=True, message="Execution completed successfully.")


def main() -> None:
    parser = argparse.ArgumentParser(prog="velktharion", description="Autonomous browser with persistent memory")
    parser.add_argument("--dry-run", action="store_true", help="Run without side effects")
    args = parser.parse_args()

    result = run(dry_run=args.dry_run)
    print(result.message)


if __name__ == "__main__":
    main()
