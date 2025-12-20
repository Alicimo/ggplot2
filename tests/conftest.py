import pytest


def _has_module(name: str) -> bool:
    try:
        __import__(name)
        return True
    except Exception:
        return False


def pytest_collection_modifyitems(config, items):
    """Skip upstream plotnine tests by default.

    The vendored suite under tests/plotnine_upstream targets matplotlib rendering
    and plotnine internals that are not yet implemented here.

    We keep the suite in-tree as a compatibility target and will gradually
    enable subsets.
    """

    for item in items:
        path = str(item.fspath)
        if "/tests/plotnine_upstream/" in path:
            item.add_marker(
                pytest.mark.skip(
                    reason="vendored plotnine upstream tests (not yet supported)"
                )
            )


def pytest_ignore_collect(collection_path, config):
    """Ignore vendored upstream suite unless explicitly enabled."""

    path_str = str(collection_path)
    if "/tests/plotnine_upstream/" not in path_str:
        return False

    # Allow opting in via -m upstream
    if config.getoption("-m") and "upstream" in str(config.getoption("-m")):
        return False

    return True


def pytest_configure(config):
    config.addinivalue_line("markers", "upstream: vendored upstream plotnine test")
    config.addinivalue_line("markers", "needs_matplotlib: requires matplotlib")
    config.addinivalue_line("markers", "needs_mizani: requires mizani")


def pytest_runtest_setup(item):
    if item.get_closest_marker("needs_matplotlib") and not _has_module("matplotlib"):
        pytest.skip("matplotlib not installed")
    if item.get_closest_marker("needs_mizani") and not _has_module("mizani"):
        pytest.skip("mizani not installed")
