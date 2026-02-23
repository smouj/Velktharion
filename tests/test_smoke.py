from src.velktharion.cli import run


def test_dry_run_smoke():
    result = run(dry_run=True)
    assert result.ok is True
