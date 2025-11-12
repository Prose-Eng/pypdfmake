from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_expected_json(filename: str) -> dict[str, Any]:
    """Return fixture contents from tests/expected_outputs."""

    fixtures_dir = Path(__file__).resolve().parent / "expected_outputs"
    with (fixtures_dir / filename).open(encoding="utf-8") as file:
        return json.load(file)
