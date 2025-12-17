"""
player.py

Defines Player class and stores run history.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from .metrics import SortMetrics


@dataclass
class Player:
    """Stores player state and run history."""
    name: str
    score: int = 0
    level_index: int = 0
    history: list[dict] = field(default_factory=list)

    def add_score(self, points: int) -> None:
        self.score += int(points)

    def advance_level(self) -> None:
        self.level_index += 1

    def record_run(self, level_id: int, algo: str, metrics: SortMetrics, earned: int) -> None:
        self.history.append(
            {
                "level_id": int(level_id),
                "algo": str(algo),
                "comparisons": int(metrics.comparisons),
                "swaps": int(metrics.swaps),
                "time_ms": float(metrics.time_ms),
                "earned": int(earned),
                "total_score": int(self.score),
            }
        )

    def __str__(self) -> str:
        return f"Player(name={self.name}, score={self.score}, level_index={self.level_index})"
