"""
io_utils.py

Handles data I/O using pandas and basic validation.
Demonstrates exception handling (try/except + custom exception).
"""

from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import json
import pandas as pd


class InvalidLevelError(Exception):
    """Raised when a level row is missing required fields or has invalid data."""


@dataclass(frozen=True)
class Level:
    """Immutable representation of a single game level."""
    level_id: int
    difficulty: int
    array: list[int]


def parse_array(array_str: str) -> list[int]:
    """Parse a space-separated string of ints into a list[int]."""
    return [int(x) for x in str(array_str).strip().split()]


def load_levels_csv(csv_path: str | Path) -> list[Level]:
    """
    Load levels from a CSV file with columns: level_id, difficulty, array
    array is a quoted string like: "5 3 1 4 2"
    """
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Could not find file: {csv_path}") from e
    except Exception as e:
        raise ValueError(f"Failed to read CSV. Check formatting: {csv_path}") from e

    required = {"level_id", "difficulty", "array"}
    if not required.issubset(set(df.columns)):
        raise InvalidLevelError(f"CSV must contain columns: {sorted(required)}")

    levels: list[Level] = []
    for idx, row in df.iterrows():
        try:
            level_id = int(row["level_id"])
            difficulty = int(row["difficulty"])
            array = parse_array(row["array"])
        except Exception as e:
            raise InvalidLevelError(f"Bad row at index {idx}: {row.to_dict()}") from e

        if difficulty < 1 or not array:
            raise InvalidLevelError(f"Invalid level data at index {idx}: {row.to_dict()}")

        levels.append(Level(level_id=level_id, difficulty=difficulty, array=array))

    return levels


def save_history_json(history: list[dict], out_path: str | Path) -> None:
    """Save player run history to JSON (meaningful output I/O)."""
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)
"""
io_utils.py

Handles data I/O using pandas and basic validation.
Demonstrates exception handling (try/except + custom exception).
"""

from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import json
import pandas as pd


class InvalidLevelError(Exception):
    """Raised when a level row is missing required fields or has invalid data."""


@dataclass(frozen=True)
class Level:
    """Immutable representation of a single game level."""
    level_id: int
    difficulty: int
    array: list[int]


def parse_array(array_str: str) -> list[int]:
    """Parse a space-separated string of ints into a list[int]."""
    return [int(x) for x in str(array_str).strip().split()]


def load_levels_csv(csv_path: str | Path) -> list[Level]:
    """
    Load levels from a CSV file with columns: level_id, difficulty, array
    array is a quoted string like: "5 3 1 4 2"
    """
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Could not find file: {csv_path}") from e
    except Exception as e:
        raise ValueError(f"Failed to read CSV. Check formatting: {csv_path}") from e

    required = {"level_id", "difficulty", "array"}
    if not required.issubset(set(df.columns)):
        raise InvalidLevelError(f"CSV must contain columns: {sorted(required)}")

    levels: list[Level] = []
    for idx, row in df.iterrows():
        try:
            level_id = int(row["level_id"])
            difficulty = int(row["difficulty"])
            array = parse_array(row["array"])
        except Exception as e:
            raise InvalidLevelError(f"Bad row at index {idx}: {row.to_dict()}") from e

        if difficulty < 1 or not array:
            raise InvalidLevelError(f"Invalid level data at index {idx}: {row.to_dict()}")

        levels.append(Level(level_id=level_id, difficulty=difficulty, array=array))

    return levels


def save_history_json(history: list[dict], out_path: str | Path) -> None:
    """Save player run history to JSON (meaningful output I/O)."""
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)
