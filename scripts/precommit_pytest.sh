#!/usr/bin/env bash
set -euo pipefail

# Run the same test command as CI.
uv run pytest -q

