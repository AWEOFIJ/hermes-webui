from pathlib import Path


SESSIONS_JS = Path(__file__).resolve().parents[1] / "static" / "sessions.js"


def test_platform_counts_do_not_recursively_rerender_sidebar():
    """Platform-count resolution must not start an endless cache-render loop."""
    src = SESSIONS_JS.read_text(encoding="utf-8")

    assert "_refreshPlatformCounts().then" not in src
    assert "if(hasNewPlatform) renderSessionListFromCache();" not in src
