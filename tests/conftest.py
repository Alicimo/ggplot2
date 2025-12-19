import pytest


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
            item.add_marker(pytest.mark.skip(reason="vendored plotnine upstream tests (not yet supported)"))

