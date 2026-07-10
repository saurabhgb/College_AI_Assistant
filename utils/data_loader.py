import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def load_json(file_path: str) -> dict:
    """Load JSON data using a path relative to the project root."""
    path = PROJECT_ROOT / file_path
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)
